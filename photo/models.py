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
        max_length=200, blank=True, null=True)
    parent=models.ForeignKey(
        ParentCategory,
        verbose_name='親カテゴリ',
        on_delete=models.PROTECT, blank=True, null=True
        )
    
    def __str__(self):
        return self.title
class Students(models.Model):
    name=models.CharField(
        verbose_name='名前',
        max_length=200, blank=True, null=True
        

         )
    student_id=models.CharField(verbose_name='生徒ID',max_length=200, blank=True, null=True
        

         )
    user=models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE, blank=True, null=True
        )   

class EnglishScore(models.Model):
    student=models.ForeignKey(
        Students,
        verbose_name='生徒',
        on_delete=models.CASCADE, blank=True, null=True
        )
    
 
    category=models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT, blank=True, null=True
        )
    


class EnglishWords(models.Model):
    word=models.CharField(
        verbose_name='英語',
        max_length=200, blank=True, null=True
        

         )
    trans=models.CharField(
        verbose_name='翻訳',
        max_length=200, blank=True, null=True
    )
  
    category=models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT, blank=True, null=True
        )
    def __str__(self):
        return self.word
  
class PhotoPost(models.Model):
    user=models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE, blank=True, null=True
        )
    category=models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT, blank=True, null=True
        )
    title=models.CharField(
        verbose_name='タイトル',
        max_length=200, blank=True, null=True
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
