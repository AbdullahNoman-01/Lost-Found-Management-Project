from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView,
    UpdateView,
    FormView,
)
from django.db.models import Q

from . import models
from . import forms


# =========================
# CREATE FOUND ITEM
# =========================

class ReportFoundItemView(FormView):

    template_name = "found_items_form.html"
    form_class = forms.ReportFoundItemForm
    success_url = reverse_lazy("report_found_item_viewer")

    def form_valid(self, form):

        # Do not allow the user to choose another user.
        # Automatically assign the currently logged-in user.
        report = form.save(commit=False)
        report.user = self.request.user
        report.save()

        messages.success(
            self.request,
            "Your found item report has been submitted successfully! 🎉"
        )

        return super().form_valid(form)


# =========================
# FOUND ITEM LIST
# =========================

class ReportFoundItemRead(ListView):

    model = models.ReportFoundItem
    template_name = "found_items_viewer.html"
    context_object_name = "found_items"

    def get_queryset(self):

        queryset = models.ReportFoundItem.objects.all()

        # Search
        search = self.request.GET.get("search", "").strip()

        if search:
            queryset = queryset.filter(
                Q(item_name__icontains=search) |
                Q(description__icontains=search) |
                Q(location_found__icontains=search) |
                Q(category__icontains=search)
            )

        # Sort
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


# =========================
# FOUND ITEM DETAIL
# =========================

class ReportFoundItemDetail(DetailView):

    model = models.ReportFoundItem
    template_name = "found_item_detail.html"
    context_object_name = "item_detail"


# =========================
# UPDATE FOUND ITEM
# =========================

class ReportFoundItemUpdate(UpdateView):

    model = models.ReportFoundItem
    form_class = forms.ReportFoundItemForm
    template_name = "found_item_update.html"
    context_object_name = "item_update"

    def form_valid(self, form):

        # Keep the original owner/user
        form.instance.user = self.get_object().user

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


# =========================
# DELETE FOUND ITEM
# =========================

class ReportFoundItemDelete(DeleteView):

    model = models.ReportFoundItem
    template_name = "found_item_delete.html"
    context_object_name = "found_item"

    success_url = reverse_lazy(
        "report_found_item_viewer"
    )

    def form_valid(self, form):

        messages.success(
            self.request,
            "Found item deleted successfully!"
        )

        return super().form_valid(form)

