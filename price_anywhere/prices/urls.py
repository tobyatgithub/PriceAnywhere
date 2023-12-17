from django.urls import path
from .views import PurchaseRecordListView

urlpatterns = [
    path('purchase_records/', PurchaseRecordListView.as_view(), name='purchase_record_list'),
    # Add more URL patterns for other views (create, update, delete) as needed
]
