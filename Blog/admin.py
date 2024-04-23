from django.contrib import admin
from .models import Blog, BlogCategory, BlogEvent

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'total_viewed', 'total_liked', 'total_shared')
    #we can also use list 

    def total_viewed(self, obj):
        return obj.total_viewed()

    def total_liked(self, obj):
        return obj.total_liked()

    def total_shared(self, obj):
        return obj.total_shared()

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_viewed', 'total_liked', 'total_shared')

    def total_viewed(self, obj):
        return sum([blog.total_viewed() for blog in obj.blog_set.all()])

    def total_liked(self, obj):
        return sum([blog.total_liked() for blog in obj.blog_set.all()])

    def total_shared(self, obj):
        return sum([blog.total_shared() for blog in obj.blog_set.all()])

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(BlogEvent)
