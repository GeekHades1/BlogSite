from django.contrib import admin
from .models import Post, Category, Tag, ShareWeb, OfferLink


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

class ShareWebAdmin(admin.ModelAdmin):
    fields = ("name", "link")

class OfferLinkAdmin(admin.ModelAdmin):
    fields = ("name", "link")

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(ShareWeb, ShareWebAdmin)
admin.site.register(OfferLink, OfferLinkAdmin)
