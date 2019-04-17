from django.contrib import admin
from .models import Post, Category, Tag, ShareWeb, OfferLink, SloganContent


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)


class ShareWebAdmin(admin.ModelAdmin):
    fields = ("name", "link")
admin.site.register(ShareWeb, ShareWebAdmin)


class OfferLinkAdmin(admin.ModelAdmin):
    fields = ("name", "link")
admin.site.register(OfferLink, OfferLinkAdmin)


class SloganAdmin(admin.ModelAdmin):
    fields = ("content", )
admin.site.register(SloganContent, SloganAdmin)
