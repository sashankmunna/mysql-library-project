from django.contrib import admin

# Register your models here.
from app0.models import Books_model

class BooksAdmin(admin.ModelAdmin):
	list_display=['Book_Name','Author','Language','Email','Genre','Sales']
admin.site.register(Books_model,BooksAdmin)