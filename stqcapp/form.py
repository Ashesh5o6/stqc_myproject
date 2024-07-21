from django import forms
from .models import dispatchform

class eddispatches(forms.ModelForm):
    class Meta:
        model = dispatchform
        fields = '__all__'