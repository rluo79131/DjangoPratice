from django import forms
from data.models import data


class DataForm(forms.ModelForm):
    class Meta:
        model = data
        fields = ['name', 'remark']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'remark': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'name': '姓名',
            'remark': '備註'
        }
