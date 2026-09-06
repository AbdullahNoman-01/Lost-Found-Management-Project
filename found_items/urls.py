from django.urls import path
from .import views
urlpatterns = [
   path('form/', views.ReportFoundItemView.as_view(), name = 'report_found_item_form'),
   
   path('view/', views.ReportFoundItemRead.as_view(), name = 'report_found_item_viewer'),

   path("<int:pk>/",views.ReportFoundItemDetail.as_view(),name="found_detail"),

   path("<int:pk>/update/",views.ReportFoundItemUpdate.as_view(),name="Found_update"),

   path("<int:pk>/delete/",views.ReportFoundItemDelete.as_view(),name="found_delete"),
]