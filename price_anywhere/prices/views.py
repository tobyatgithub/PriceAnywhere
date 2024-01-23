from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import PurchaseRecord
from .forms import PurchaseRecordForm

class PurchaseRecordListView(ListView):
    model = PurchaseRecord
    template_name = 'prices/purchase_record_list.html'
    context_object_name = 'purchase_records'

class PurchaseRecordCreateView(CreateView):
    model = PurchaseRecord
    form_class = PurchaseRecordForm
    template_name = 'prices/purchase_record_form.html'
    success_url = reverse_lazy('purchase_record_list')

class PurchaseRecordUpdateView(UpdateView):
    model = PurchaseRecord
    form_class = PurchaseRecordForm
    template_name = 'prices/purchase_record_form.html'
    success_url = reverse_lazy('purchase_record_list')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        # Prepopulate the form with existing data for editing
        form.instance = self.get_object()
        return super().form_valid(form)
    
class PurchaseRecordDeleteView(DeleteView):
    model = PurchaseRecord
    template_name = 'prices/purchase_record_confirm_delete.html'
    success_url = reverse_lazy('purchase_record_list')
    

def home(request):
    return render(request, 'prices/purchase_record_list.html')