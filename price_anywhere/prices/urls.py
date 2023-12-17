from django.urls import path
from .views import PurchaseRecordListView, PurchaseRecordCreateView, PurchaseRecordUpdateView

urlpatterns = [
    path('purchase_records/', PurchaseRecordListView.as_view(), name='purchase_record_list'),
    path('purchase_records/add/', PurchaseRecordCreateView.as_view(), name='purchase_record_add'),
    path('purchase_records/<int:pk>/edit/', PurchaseRecordUpdateView.as_view(), name='purchase_record_edit'),
    # Add more URL patterns for other views (create, update, delete) as needed
]
