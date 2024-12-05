# -*- coding: utf-8 -*-

from django.urls import path
from .import views
app_name='photo'
urlpatterns=[path('',views.IndexView.as_view(),name='index'),
             
             path('post/',views.CreatePhotoView.as_view(),name='post'),
             path('post_done/',views.PostSuccessView.as_view(),name='post_done'),
             path('photos/<int:category>',
                  views.CategoryView.as_view(),
                  name='photos_cat'
                  ),
             path('user-list/<int:user>',
                  views.UserView.as_view(),
                  name='user_list'
                  ),
             path('photo-detail/<int:pk>',
                  views.DetailView.as_view(),
                  name='photo_detail'
                  ),
             path('mypage/',views.MypageView.as_view(), name='mypage'),
             path('photo/<int:pk>/delete/',
                  views.PhotoDeleteView.as_view(),
                  name='photo_delete'),
             path('typing/',views.TypingView.as_view(), name='typing'),
             path('process/',views.process, name='process'),
             path('create/',views.CreateView.as_view(),name='create'),
             path('api/category/get/', views.ajax_get_category, name='ajax_get_category'),
             path('createcategory/',views.CreateCategoryView.as_view(),name='createcategory'),
             path('createparentcategory/',views.CreateParentCategoryView.as_view(),name='createparentcategory'),
             
             path('api/printlist/get/', views.ajax_get_printlist, name='ajax_get_printlist'),
             path('api/deleteparentcategory/get/', views.ajax_get_deleteparentcategory, name='ajax_get_deleteparentcategory'),
             path('api/createparentcategory/get/', views.ajax_get_createparentcategory, name='ajax_get_createparentcategory'),
             path('api/createcategory/get/', views.ajax_get_createcategory, name='ajax_get_createcategory'),
             path('api/deletecategory/get/', views.ajax_get_deletecategory, name='ajax_get_deletecategory'),

]
