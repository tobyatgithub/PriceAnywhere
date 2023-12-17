from django.urls import path
from .views import PurchaseRecordListView, PurchaseRecordCreateView

urlpatterns = [
    path('purchase_records/', PurchaseRecordListView.as_view(), name='purchase_record_list'),
    path('purchase_records/add/', PurchaseRecordCreateView.as_view(), name='purchase_record_add'),
    # Add more URL patterns for other views (create, update, delete) as needed
]
