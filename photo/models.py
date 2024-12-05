from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
class ParentCategory(models.Model):
    title=models.CharField(
        verbose_name='親カテゴリ',
        max_length=200,
        blank=True, 
        null=True
    )    
    def __str__(self):
       return self.title
    

class Category(models.Model):
    title=models.CharField(
        verbose_name='カテゴリ',
        max_length=200)
    parent=models.ForeignKey(
        ParentCategory,
        verbose_name='親カテゴリ',
        on_delete=models.PROTECT
        )
    
    def __str__(self):
        return self.title

class EnglishScore(models.Model):
    user=models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
        )
    
 
    category=models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT
        )
    
    def __str__(self):
        return self.user


class EnglishWords(models.Model):
    word=models.CharField(
        verbose_name='英語',
        max_length=200
        

         )
    trans=models.CharField(
        verbose_name='翻訳',
        max_length=200
    )
  
    category=models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT
        )
    def __str__(self):
        return self.word
  
class PhotoPost(models.Model):
    user=models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
        )
    category=models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT
        )
    title=models.CharField(
        verbose_name='タイトル',
        max_length=200
        )
    comment=models.TextField(
        verbose_name='コメント',
        )
    image1 =models.ImageField(
        verbose_name='イメージ1',
        upload_to='photos'
        )
    image2 =models.ImageField(
        verbose_name='イメージ２',
        upload_to='photos',
        blank=True,
        null=True
        )
    posted_at=models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
        )
    
    def __str__(self):
        return self.title
# Create your models here.
