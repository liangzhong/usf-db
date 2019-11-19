from django import forms
# from django.db import models
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Ebook, Publisher, Vendor, Author

class NewEbookForm(forms.ModelForm):
  #publisher = forms.CharField(widget=forms.Textarea(attrs={'row':1, 'cols':30, 'style': 'height: 2em;'}), max_length=30)
  # vendor = forms.CharField(widget=forms.Textarea(attrs={'row':1, 'cols':30, 'style': 'height: 2em;'}), max_length=30)
  publisher = forms.ModelChoiceField(queryset=Publisher.objects.all().order_by('pk'))
  vendor = forms.ModelChoiceField(queryset=Vendor.objects.all().order_by('pk'))
  author = forms.ModelMultipleChoiceField(
      label="Something",
      widget=FilteredSelectMultiple("Author", is_stacked=False, attrs={'rows':'5'}),
      queryset=Author.objects.all())
  class Meta:
    model = Ebook
    fields = ['title', 'url']

  class Media:
    css = {
            'all': ('/static/admin/css/widgets.css',),
            }
    js = ('/admin/jsi18n',)

    def clean_drg_choise(self):
      drg_choise = self.cleaned_data['drg_choise']
      return drg_choise  


class NewPublisherForm(forms.ModelForm):
  class Meta:
    model = Publisher
    fields = ['name', 'address']