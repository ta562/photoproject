from django.contrib import admin
from .models import Category,PhotoPost,EnglishWords,EnglishScore,ParentCategory
class ParentCategoryAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links=('id','title')
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','title','parent')
    list_display_links=('id','title')

class PhotoPostAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links=('id','title')
class EnglishWordsAdmin(admin.ModelAdmin):
    
    
    
    list_display=('id','word','category')
    list_display_links=('id','word')

class EnglishScoreAdmin(admin.ModelAdmin):
    list_display=('id','user')
    list_display_links=('id','user')
admin.site.register(ParentCategory,ParentCategoryAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(PhotoPost,PhotoPostAdmin)
admin.site.register(EnglishWords,EnglishWordsAdmin)
admin.site.register(EnglishScore,EnglishScoreAdmin)
# Register your models here.
