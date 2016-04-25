#encoding: utf-8
from betterforms.forms import Fieldset
from partners.models import Partner
from betterforms import forms as b_forms
from django import forms



class PartnerForm(b_forms.BetterModelForm):

    class Meta:
        model = Partner
        fields = [
            'club','username','password','photo','email', 'is_superuser', 'is_staff', 'is_approved', 'is_active',
            'first_name', 'last_name', 'doc_id', 'birth_date', 'gender', 'rh', 'phone', 'address', 'dni_support',
            'reference_letter', 'request_letter', 'release_letter', 'eps_affiliation', 'legal_records', 'bank_deposit',
        ]

        widgets={
            'club': forms.Select(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'photo':forms.FileInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'is_active': forms.TextInput(attrs={'class':'access-hide'}),
            'is_superuser':forms.TextInput(attrs={'class':'access-hide'}),
            'is_staff':forms.TextInput(attrs={'class':'access-hide'}),
            'is_approved':forms.TextInput(attrs={'class':'access-hide'}),
            'rh':forms.Select(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'doc_id':forms.NumberInput(attrs={'class':'form-control'}),
            'birth_date':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.widgets.Select(choices=Partner.GENDERS, attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'dni_support': forms.FileInput(attrs={'class':'form-control'}),
            'reference_letter': forms.FileInput(attrs={'class':'form-control'}),
            'request_letter': forms.FileInput(attrs={'class':'form-control'}),
            'release_letter': forms.FileInput(attrs={'class':'form-control'}),
            'eps_affiliation': forms.FileInput(attrs={'class':'form-control'}),
            'legal_records': forms.FileInput(attrs={'class':'form-control'}),
            'bank_deposit': forms.FileInput(attrs={'class':'form-control'}),
        }

        labels = {
            'is_staff': 'Administrador', 'is_superuser': 'Superusuario'
        }

        fieldsets = (

            Fieldset('cuenta', fields=(
                'club','username','password','email', 'is_superuser', 'is_staff',  'is_active', 'is_approved','photo'
            ), legend=u'1. Información de la cuenta'),

            Fieldset('personal', fields=(
                'first_name', 'last_name', 'doc_id', 'birth_date', 'gender', 'rh','phone',
                'address',
            ), legend=u'2. Información personal'),

            Fieldset('soportes', fields=(
                'dni_support', 'reference_letter', 'request_letter', 'release_letter',
                'eps_affiliation', 'legal_records', 'bank_deposit',
            ), legend=u'3. Soportes'),
        )
