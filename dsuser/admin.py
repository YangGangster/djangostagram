from django.contrib import admin

from dsuser.models import Dsuser

# Register your models here.
class DsuserAdmin(admin.ModelAdmin):
    list_display = ('userId','password')

admin.site.register(Dsuser,DsuserAdmin)