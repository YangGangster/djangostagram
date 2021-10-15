from django.contrib import admin

from dspost.models import Post

# Register your models here.
class DspostAdmin(admin.ModelAdmin):
    list_display = ('title','author')

admin.site.register(Post,DspostAdmin)