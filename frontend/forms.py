#encoding: utf-8
from betterforms.forms import Fieldset
from django.contrib.admin.forms import AdminPasswordChangeForm
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.core.urlresolvers import reverse_lazy
from django.forms.utils import flatatt
from django.forms.widgets import Widget
from django.utils.html import format_html
from partners.models import Partner
from betterforms import forms as b_forms
from django import forms

class AffiliationForm(b_forms.BetterModelForm):

    def __init__(self, *args, **kwargs):
        super(AffiliationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    def save(self, commit=True):
        user = super(AffiliationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user

    class Meta:
        model = Partner
        fields = [
            'club','username','password','photo','email','first_name', 'last_name', 'doc_id', 'birth_date', 'gender',
            'rh', 'phone', 'address', 'dni_support', 'reference_letter', 'request_letter', 'release_letter',
            'eps_affiliation', 'legal_records', 'bank_deposit',
        ]

        widgets={
            'club': forms.Select(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'photo':forms.FileInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
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

        fieldsets = (

            Fieldset('cuenta', fields=(
                'club','photo','username','password','email'
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