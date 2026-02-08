from django import forms
from .models import Rig

class RigForm(forms.ModelForm):
    class Meta:
        model = Rig
        fields = ['name', 'description', 'components']
        widgets = {
            'components': forms.CheckboxSelectMultiple(), # select parts
        }