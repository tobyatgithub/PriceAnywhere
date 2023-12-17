from django.shortcuts import render
from django.views.generic import ListView
from .models import PurchaseRecord

# Create your views here.
class PurchaseRecordListView(ListView):
    model = PurchaseRecord
    template_name = 'prices/purchase_record_list.html'
    context_object_name = 'purchase_records'