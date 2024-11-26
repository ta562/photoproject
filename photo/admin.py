from django.contrib import admin
from .models import Category,PhotoPost,EnglishWords,EnglishsScore
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links=('id','title')
class PhotoPostAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links=('id','title')
class EnglishWordsAdmin(admin.ModelAdmin):
    list_display=('id','word')
    list_display_links=('id','word')
class EnglishsScoreAdmin(admin.ModelAdmin):
    list_display=('id','user')
    list_display_links=('id','user')

admin.site.register(Category,CategoryAdmin)
admin.site.register(PhotoPost,PhotoPostAdmin)
admin.site.register(EnglishWords,EnglishWordsAdmin)
admin.site.register(EnglishsScore,EnglishsScoreAdmin)
# Register your models here.
