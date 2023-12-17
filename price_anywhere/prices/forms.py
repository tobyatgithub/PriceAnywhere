from django import forms
from .models import PurchaseRecord

class PurchaseRecordForm(forms.ModelForm):
    class Meta:
        model = PurchaseRecord
        fields = '__all__'