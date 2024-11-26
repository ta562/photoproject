# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:17:15 2024

@author: Htomo
"""
from django.forms import ModelForm
from .models import PhotoPost
from .models import EnglishWords
class PhotoPostForm(ModelForm):
    class Meta:
        model=PhotoPost
        fields=['category','title','comment','image1','image2']

class EnglishWordsForm(ModelForm):
    class Meta:
        model=EnglishWords
        fields=['word','trans']