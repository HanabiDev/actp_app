from django import forms
from partners.models import Partner


class PartnerForm(forms.ModelForm):

    class Meta:
        model = Partner
        fields = ['club', 'first_name', 'last_name', 'doc_id', 'birth_date', 'gender', 'phone', 'address', 'photo' ]

        widgets={
            'club':forms.Select(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'doc_id':forms.NumberInput(attrs={'class':'form-control'}),
            'birth_date':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.widgets.Select(choices=Partner.GENDERS, attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'photo': forms.FileInput(attrs={'class':'form-control'}),
        }
