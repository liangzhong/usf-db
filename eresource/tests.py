from django.test import TestCase
from django.urls import reverse, resolve

from .views import home, ebook_detail
from .models import Ebook

# Create your tests here.
class HomeTests(TestCase):
  def setUp(self):
    self.Ebook = Ebook.objects.create(title='AAA', author='BBB', url='http://ccc.ddd' )
    url = reverse('home')
    self.response = self.client.get(url)

  def test_home_view_status_code(self):
    # url = reverse('/')
    # response = self.client.get(url)
    self.assertEquals(self.response.status_code, 200)

  def test_home_url_resolves_home_view(self):
    view = resolve('/')
    self.assertEquals(view.func, home)

  def test_home_view_contains_link_to_ebook_detail_page(self):
    ebook_detail_url = reverse('ebook_detail', kwargs={'pk': self.Ebook.pk})
    self.assertEquals(self.response, 'href="{0}"'.format(ebook_detail_url))


class EbooksEbookTest(TestCase):
  def setUp(self):
    Ebook.objects.create(title='AAA', author='BBB', url='http://ccc.ddd' )

  def test_ebook_detail_view_success_status_code(self):
    url = reverse('ebook_detail', kwargs={'pk':1})
    response = self.client.get(url)
    self.assertEquals(response.status_code, 200)

  def test_ebook_detail_view_not_found_status_code(self):
    url = reverse('ebook_detail', kwargs={'pk':99})
    response = self.client.get(url)
    self.assertEquals(response.status_code, 404)

  def test_ebook_detail_url_resolves_ebook_detail_view(self):
    view = resolve('/ebooks/1/')
    self.assertEquals(view.func, ebook_detail)

