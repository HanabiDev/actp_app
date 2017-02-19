#encoding: utf-8
from betterforms.forms import Fieldset
from django.contrib.admin.forms import AdminPasswordChangeForm
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.core.urlresolvers import reverse_lazy
from django.forms.utils import flatatt
from django.forms.widgets import Widget
from django.utils.html import format_html
from partners.models import Partner, Equipment
from betterforms import forms as b_forms
from django import forms


class Button(Widget):
    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs)
        return format_html(u'<a{}>Cambiar contraseña</a>', (flatatt(final_attrs)))

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['bank_deposit']

class PartnerForm(b_forms.BetterModelForm):

    def __init__(self, *args, **kwargs):
        super(PartnerForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    def save(self, commit=True):
        user = super(PartnerForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user

    class Meta:
        model = Partner
        fields = [
            'club','username','password','photo','member_since', 'email', 'is_superuser', 'is_staff', 'is_approved', 'is_active',
            'first_name', 'last_name', 'doc_id', 'birth_date', 'gender', 'rh', 'phone', 'address',
            'occupation', 'work_phone','work_address','emergency_contact','emergency_phone','have_disease','disease_name','observations',
            'dni_support', 'reference_letter', 'request_letter', 'release_letter', 'eps_affiliation', 'legal_records', 'bank_deposit',
        ]

        widgets={
            'club': forms.Select(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'photo':forms.FileInput(attrs={'class':'form-control'}),
            'member_since': forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class':'access-hide'}),
            'is_superuser':forms.CheckboxInput(attrs={'class':'access-hide'}),
            'is_staff':forms.CheckboxInput(attrs={'class':'access-hide'}),
            'is_approved':forms.CheckboxInput(attrs={'class':'access-hide'}),
            'rh':forms.Select(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'doc_id':forms.NumberInput(attrs={'class':'form-control'}),
            'birth_date':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.widgets.Select(choices=Partner.GENDERS, attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'occupation': forms.TextInput(attrs={'class':'form-control'}),
            'work_phone': forms.TextInput(attrs={'class':'form-control'}),
            'work_address': forms.TextInput(attrs={'class':'form-control'}),
            'emergency_contact': forms.TextInput(attrs={'class':'form-control'}),
            'emergency_phone': forms.TextInput(attrs={'class':'form-control'}),
            'have_disease': forms.CheckboxInput(attrs={'class':'access-hide'}),
            'disease_name': forms.TextInput(attrs={'class':'form-control'}),
            'observations': forms.Textarea(attrs={'class':'form-control', 'rows':5, 'cols':39}),
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
                'club','photo','username','password','email','member_since','is_superuser','is_staff','is_active','is_approved'
            ), legend=u'1. Información de la cuenta'),

            Fieldset('personal', fields=(
                'first_name', 'last_name', 'doc_id', 'birth_date', 'gender', 'rh','phone',
                'address','occupation', 'work_phone','work_address'
            ), legend=u'2. Información personal'),

            Fieldset('additional', fields=(
                'emergency_contact','emergency_phone','have_disease',
                'disease_name','observations'
            ), legend=u'3. Información adicional'),

            Fieldset('soportes', fields=(
                'dni_support', 'reference_letter', 'request_letter', 'release_letter',
                'eps_affiliation', 'legal_records', 'bank_deposit',
            ), legend=u'4. Soportes'),
        )


class EditPartnerForm(b_forms.BetterModelForm):
    def __init__(self, *args, **kwargs):
        super(EditPartnerForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['password'].required = False
        self.fields['password'].widget = Button(attrs={'class':'btn waves-attach col-xs-12', 'href':reverse_lazy('partners:pass', kwargs={'partner_id':self.instance.id})})

    class Meta:
        model = Partner
        fields = [
            'club','username','password','photo','member_since', 'email', 'is_superuser', 'is_staff', 'is_approved', 'is_active',
            'first_name', 'last_name', 'doc_id', 'birth_date', 'gender', 'rh', 'phone', 'address',
            'occupation', 'work_phone','work_address','emergency_contact','emergency_phone','have_disease','disease_name','observations',
            'dni_support', 'reference_letter', 'request_letter', 'release_letter', 'eps_affiliation', 'legal_records', 'bank_deposit',
        ]

        widgets={
            'club': forms.Select(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            #'password':Button(attrs={'class':'btn waves-attach col-xs-12', 'href':reverse_lazy('partners:edit',kwargs={'partner_id': EditPartnerForm._meta.get_id()})}),
            'photo':forms.FileInput(attrs={'class':'form-control'}),
            'member_since': forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class':'access-hide'}),
            'is_superuser':forms.CheckboxInput(attrs={'class':'access-hide'}),
            'is_staff':forms.CheckboxInput(attrs={'class':'access-hide'}),
            'is_approved':forms.CheckboxInput(attrs={'class':'access-hide'}),
            'rh':forms.Select(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'doc_id':forms.NumberInput(attrs={'class':'form-control'}),
            'birth_date':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.widgets.Select(choices=Partner.GENDERS, attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'occupation': forms.TextInput(attrs={'class':'form-control'}),
            'work_phone': forms.TextInput(attrs={'class':'form-control'}),
            'work_address': forms.TextInput(attrs={'class':'form-control'}),
            'emergency_contact': forms.TextInput(attrs={'class':'form-control'}),
            'emergency_phone': forms.TextInput(attrs={'class':'form-control'}),
            'have_disease': forms.CheckboxInput(attrs={'class':'access-hide'}),
            'disease_name': forms.TextInput(attrs={'class':'form-control'}),
            'observations': forms.Textarea(attrs={'class':'form-control', 'rows':5, 'cols':39}),
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
                'club','photo','username','password','email','member_since','is_superuser','is_staff','is_active','is_approved'
            ), legend=u'1. Información de la cuenta'),

           Fieldset('personal', fields=(
                'first_name', 'last_name', 'doc_id', 'birth_date', 'gender', 'rh','phone',
                'address','occupation', 'work_phone','work_address'
            ), legend=u'2. Información personal'),

            Fieldset('additional', fields=(
                'emergency_contact','emergency_phone','have_disease',
                'disease_name','observations'
            ), legend=u'3. Información adicional'),

            Fieldset('soportes', fields=(
                'dni_support', 'reference_letter', 'request_letter', 'release_letter',
                'eps_affiliation', 'legal_records', 'bank_deposit',
            ), legend=u'4. Soportes'),
        )
        
        
class PasswordForm(SetPasswordForm):


    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].label = "Contraseña nueva"
        self.fields['new_password2'].label = "Contraseña nueva (confirmación)"
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={'class':'form-control'})
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={'class':'form-control'})


    class Meta:
        model = Partner
        exclude = '__all__'

        widgets = {
            'new_password1':forms.PasswordInput(attrs={'class':'form-control'})
        }


class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        exclude = ['owner']