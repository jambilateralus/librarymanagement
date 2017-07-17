from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Student)
admin.site.register(models.Category)
admin.site.register(models.Publisher)
admin.site.register(models.Author)
admin.site.register(models.Book)
admin.site.register(models.Burrower)
admin.site.register(models.BookCopy)
admin.site.register(models.BurrowedBook)