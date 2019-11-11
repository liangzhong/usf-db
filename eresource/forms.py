from django import forms
from .models import Ebook, Publisher, Vendor

class NewEbookForm(forms.ModelForm):
  #publisher = forms.CharField(widget=forms.Textarea(attrs={'row':1, 'cols':30, 'style': 'height: 2em;'}), max_length=30)
  publisher = forms.ModelChoiceField(queryset=Publisher.objects.all().order_by('name'))
  vendor = forms.CharField(widget=forms.Textarea(attrs={'row':1, 'cols':30, 'style': 'height: 2em;'}), max_length=30)

  class Meta:
    model = Ebook
    fields = ['title', 'author', 'url']