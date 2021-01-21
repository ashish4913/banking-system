from django import forms
from .models import Transfer
class transferform(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ['tx_to','amount']