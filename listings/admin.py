from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display=('id','username','invoice','status','ref')
    list_display_links=('id','username')
    list_filter=('status','username')
    

admin.site.register(Listing,ListingAdmin)
