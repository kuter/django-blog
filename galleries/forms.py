from django import forms


class GalleryItemInlineForm(forms.ModelForm):
    order = forms.CharField(widget=forms.HiddenInput())
