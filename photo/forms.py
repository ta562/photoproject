# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:17:15 2024

@author: Htomo
"""
from django.forms import ModelForm
from django import forms
from .models import PhotoPost
from .models import EnglishWords,EnglishScore,ParentCategory,Category
class PhotoPostForm(ModelForm):
    class Meta:
        model=PhotoPost
        fields=['category','title','comment','image1','image2']

class EnglishWordsCreateForm(forms.ModelForm):
    parent_category=forms.ModelChoiceField(
        label='親カテゴリ',
        queryset=ParentCategory.objects,
        required=False
    )
    class Meta:
        model=EnglishWords
        fields=['word','trans','parent_category','category']

class EnglishWordsTypingForm(forms.ModelForm):
    parent_category=forms.ModelChoiceField(
        label='教材',
        queryset=ParentCategory.objects,
        required=False
    )
    class Meta:
        model=EnglishWords
        fields=['parent_category','category']

class CategoryCreateForm(forms.ModelForm):
  

    class Meta:
        model=Category
        fields=['parent']

class ParentCategoryCreateForm(forms.ModelForm):
  

    class Meta:
        model=ParentCategory
        fields=['title']
