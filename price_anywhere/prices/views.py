from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import PurchaseRecord
from .forms import PurchaseRecordForm

# Create your views here.
class PurchaseRecordCreateView(CreateView):
    model = PurchaseRecord
    form_class = PurchaseRecordForm
    template_name = 'prices/purchase_record_form.html'
    success_url = reverse_lazy('purchase_record_list')

class PurchaseRecordListView(ListView):
    model = PurchaseRecord
    template_name = 'prices/purchase_record_list.html'
    context_object_name = 'purchase_records'