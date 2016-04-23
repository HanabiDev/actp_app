from django import forms
from clubs.models import Club


class ClubForm(forms.ModelForm):

    class Meta:
        model = Club
        fields = '__all__'

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'logo':forms.FileInput(attrs={'class':'form-control'}),
            'header_image':forms.FileInput(attrs={'class':'form-control'}),
            'header_description':forms.TextInput(attrs={'class':'form-control'}),
            'president':forms.Select(attrs={'class':'form-control'}),
            'foundation':forms.TextInput(attrs={'class':'form-control'}),
            'is_active':forms.CheckboxInput(attrs={'class':'access-hide'}),
            'website':forms.URLInput(attrs={'class':'form-control'}),
            'fb_page':forms.URLInput(attrs={'class':'form-control'}),
            'tw_page':forms.URLInput(attrs={'class':'form-control'}),
            'yt_page':forms.URLInput(attrs={'class':'form-control'}),
          'related_articles':forms.SelectMultiple(attrs={'class':'form-control'}),
          'related_documents':forms.SelectMultiple(attrs={'class':'form-control'}),
        }
