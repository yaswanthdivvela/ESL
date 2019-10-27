from django.contrib import admin

from .models import Acc

class AccAdmin(admin.ModelAdmin):
    list_display=('id','username','isgov')
    list_display_links=('id','username')
    list_filter=('isgov',)
    list_editable=('isgov',)
    

admin.site.register(Acc,AccAdmin)
