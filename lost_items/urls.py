from django.urls import include, path
from .import views
urlpatterns = [
    path('form/', views.ReportLostItemView.as_view(), name = 'report_lost_item'),

    path('views/', views.ReportLostItemRead.as_view(), name = 'report_lost_item_read'),

    path("<int:pk>/",views.ReportLostItemDetail.as_view(),name="lost_detail"),

    path("<int:pk>/update/",views.ReportLostItemUpdate.as_view(),name="lost_update"),

    path("<int:pk>/delete/",views.ReportLostItemDelete.as_view(),name="lost_delete"),
]
    