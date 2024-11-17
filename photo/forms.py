# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:17:15 2024

@author: Htomo
"""
from django.forms import ModelForm
from .models import PhotoPost

class PhotoPostForm(ModelForm):
    class Meta:
        model=PhotoPost
        fields=['category','title','comment','image1','image2']
