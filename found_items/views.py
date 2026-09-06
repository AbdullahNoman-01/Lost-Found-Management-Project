from django.contrib import messages 
from django.urls import reverse_lazy
from django.views.generic import ListView,DeleteView,DetailView,UpdateView,CreateView,FormView
from django.db.models import Q

from .import models
from .import forms

class ReportFoundItemView(FormView):
    template_name = 'found_items_form.html'
    form_class = forms.ReportFoundItemForm
    success_url = reverse_lazy('report_found_item_viewer')
    def form_valid(self, form):
        form.save()
        messages.success(
            self.request,
            "Your found item report has been submitted successfully! 🎉"
        )
        return super().form_valid(form)

class ReportFoundItemRead(ListView):
    model = models.ReportFoundItem
    template_name = "found_items_viewer.html"
    context_object_name = "found_items"
    def get_queryset(self):
        queryset = models.ReportFoundItem.objects.all()
        search = self.request.GET.get("search", "").strip()
        if search:
            queryset = queryset.filter(
                Q(item_name__icontains=search) |
                Q(description__icontains=search) |
                Q(location_found__icontains=search) |
                Q(category__icontains=search)
            )
        sort = self.request.GET.get("sort", "item_name")

        allowed_sort = [
            "item_name",
            "-item_name",
            "date_found",
            "-date_found",
        ]
        if sort in allowed_sort:
            queryset = queryset.order_by(sort)
        else:
            queryset = queryset.order_by("item_name")
        return queryset


class ReportFoundItemDetail(DetailView):
    model = models.ReportFoundItem
    template_name = "found_item_detail.html"
    context_object_name = "item_detail"


class ReportFoundItemUpdate(UpdateView):
    model = models.ReportFoundItem
    form_class = forms.ReportFoundItemForm
    template_name = "found_item_update.html"
    context_object_name = "item_update"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            "Found item updated successfully!"
        )
        return response
    def get_success_url(self):
        return reverse_lazy(
            "found_detail",
            kwargs={"pk": self.object.pk}
        )
    
class ReportFoundItemDelete(DeleteView):
    model = models.ReportFoundItem
    template_name = "found_item_delete.html"
    context_object_name = "found_item"
    success_url = reverse_lazy("report_found_item_viewer")
    def form_valid(self, form):
        messages.success(
            self.request,
            "Lost item deleted successfully!"
        )
        return super().form_valid(form)
    