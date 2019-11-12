from django import forms
from .models import Ebook, Publisher, Vendor

class NewEbookForm(forms.ModelForm):
  #publisher = forms.CharField(widget=forms.Textarea(attrs={'row':1, 'cols':30, 'style': 'height: 2em;'}), max_length=30)
  # vendor = forms.CharField(widget=forms.Textarea(attrs={'row':1, 'cols':30, 'style': 'height: 2em;'}), max_length=30)
  publisher = forms.ModelChoiceField(queryset=Publisher.objects.all().order_by('pk'))
  vendor = forms.ModelChoiceField(queryset=Vendor.objects.all().order_by('pk'))
  
  class Meta:
    model = Ebook
    fields = ['title', 'author', 'url']

class NewPublisherForm(forms.ModelForm):
  class Meta:
    model = Publisher
    fields = ['name', 'address']    