from django.contrib import admin
from .models import Ebook
from .models import Publisher
from .models import Vendor, Author

admin.site.register(Ebook)
admin.site.register(Publisher)
admin.site.register(Vendor)
admin.site.register(Author)

