from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
from django.http import Http404
from .forms import NewEbookForm, NewPublisherForm

from .models import Ebook, Publisher, Vendor, Author


def home(request):
    ebooks = Ebook.objects.all()
    return render(request, 'home.html', {'ebooks': ebooks})


def ebook_detail(request, pk):
    try:
        ebook = Ebook.objects.get(pk=pk)
    except Ebook.DoesNotExist:
        raise Http404
    return render(request, 'ebook_detail.html', {'ebook': ebook})


def browse_book(request, status_filter=None):
    if status_filter and status_filter != "0":
      ebooks = Ebook.objects.filter(publisher=status_filter)   
    else:
      ebooks = Ebook.objects.all()
    publishers = Publisher.objects.all()
    return render(request, 'browse_book.html', {'ebooks': ebooks, 'publishers': publishers, 'status_filter': status_filter})

def search_results(request):
  if request.method == 'GET':  
    author_name=request.GET.get('author')
    ebooks = Ebook.objects.filter(author__icontains=author_name)
  return render(request, 'search_result.html', {'ebooks': ebooks})

def search_book(request):
  return render(request, 'search_book.html')

def add_publisher(request):
  if request.method == 'POST':
    form = NewPublisherForm(request.POST)
    if form.is_valid():
      # TODO: check if the publisher is already exists by name
      form.save()
  else:
    form = NewPublisherForm()
  return render(request, 'add_publisher.html', {'form': form})    


def add_book(request):
  user = User.objects.first()  # TODO: get the currently logged in user
  if request.method == 'POST':
    form = NewEbookForm(request.POST)
    if form.is_valid():
      ebook = form.save(commit=False)
      ebook.vendor = Vendor.objects.get(pk=(request.POST.get('vendor')))
      ebook.publisher = Publisher.objects.get(pk=(request.POST.get('publisher')))
      ebook.author = Author.objects.get(pk=(request.POST.get('author'))) # TODO 
      ebook.create_by = user
      ebook.save()
      # TODO: redirect to the created topic page
      return redirect('browse_book')
  else:
    form = NewEbookForm()
  return render(request, 'add_book.html', {'form': form})

    # return render(request, 'add_book.html')
# if(request.POST.publisher not in Publisher.objects.all()):
    #   p = Publisher.objects.create(
    #     name=form.cleaned_data.get('publisher'),
    #   )
    # else:
    #   p = Publisher.objects.get(name=form.cleaned_data.get('publisher'))

    # if(request.POST.vendor not in Vendor.objects.all()):
    #   v = Vendor.objects.create(
    #     name=form.cleaned_data.get('vendor'),
    # )
    # else:
    #   v = Vendor.objects.get(name=form.cleaned_data.get('vendor'))
