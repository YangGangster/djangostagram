from django.contrib import admin

from dspost.models import Dspost, Tag

# Register your models here.
class DspostAdmin(admin.ModelAdmin):
    list_display = ('title','author')

class DsTagAdmin(admin.ModelAdmin):
    list_display = ('name','registered_date')

admin.site.register(Dspost,DspostAdmin)
admin.site.register(Tag,DsTagAdmin)