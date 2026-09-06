from django.views.generic import DeleteView, DetailView, FormView, ListView, UpdateView 
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ReportLostItemForm
from .import models
from django.shortcuts import redirect
from django.db.models import Q

class ReportLostItemView(FormView):
    template_name = 'lost_items.html'
    form_class = ReportLostItemForm
    success_url = reverse_lazy('report_lost_item_read')
    def form_valid(self, form):
        form.save()
        messages.success(
            self.request,
            "Your lost item report has been submitted successfully! 🎉"
        )
        return super().form_valid(form)


class ReportLostItemRead(ListView):
    model = models.ReportLostItem
    template_name = "lost_items_view.html"
    context_object_name = "lost_items"
    def get_queryset(self):
        queryset = models.ReportLostItem.objects.all()

        search = self.request.GET.get("search", "").strip()

        if search:
            queryset = queryset.filter(
                Q(item_name__icontains=search) |
                Q(description__icontains=search) |
                Q(location_lost__icontains=search) |
                Q(category__icontains=search)
            )

        sort = self.request.GET.get("sort", "item_name")

        allowed_sort = [
            "item_name",
            "-item_name",
            "date_lost",
            "-date_lost",
        ]

        if sort in allowed_sort:
            queryset = queryset.order_by(sort)
        else:
            queryset = queryset.order_by("item_name")

        return queryset


class ReportLostItemDetail(DetailView):
    model = models.ReportLostItem
    template_name = "lost_item_detail.html"
    context_object_name = "item"


class ReportLostItemUpdate(UpdateView):
    model = models.ReportLostItem
    form_class = ReportLostItemForm
    template_name = "lost_item_update.html"
    context_object_name = "item"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            "Lost item updated successfully!"
        )
        return response
    def get_success_url(self):
        return reverse_lazy(
            "lost_detail",
            kwargs={"pk": self.object.pk}
        )
    
class ReportLostItemDelete(DeleteView):
    model = models.ReportLostItem
    template_name = "lost_item_delete.html"
    context_object_name = "item"
    success_url = reverse_lazy("report_lost_item_read")
    def form_valid(self, form):
        messages.success(
            self.request,
            "Lost item deleted successfully!"
        )
        return super().form_valid(form)
    