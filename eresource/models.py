from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vendor(models.Model):
  name = models.CharField(max_length=30, unique=True)
  address = models.CharField(max_length=30, null=True)
  contact = models.CharField(max_length=20,null=True)

  def __str__(self):
    return self.name


class Publisher(models.Model):
  name = models.CharField(max_length=30, unique=True)
  address = models.CharField(max_length=30, null=True)

  def __str__(self):
    return self.name


class Author(models.Model):
  name = models.CharField(max_length=30)
  description = models.CharField(max_length=200, blank=True, null=True)

  def __str__(self):
    return self.name


class Ebook(models.Model):
  title = models.CharField(max_length=30)
  author = models.ManyToManyField(Author)
  url = models.URLField(max_length=100)
  vendor = models.ForeignKey(Vendor, related_name='ebooks', max_length=30, blank=True, null=True, on_delete=models.SET_NULL)
  publisher = models.ForeignKey(Publisher, related_name='ebooks', max_length=30, blank=True, null=True, on_delete=models.SET_NULL)
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now_add=True, null=True)
  create_by = models.ForeignKey(User, related_name='+', blank=True, null=True, on_delete=models.SET_NULL)
  update_by = models.ForeignKey(User, related_name='+', blank=True, null=True, on_delete=models.SET_NULL)

  def __str__(self):
    return self.title


