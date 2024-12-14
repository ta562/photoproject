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
             path('typing/<str:pk>',views.TypingView.as_view(), name='typing'),
             path('process/',views.process, name='process'),
             path('create/',views.CreateView.as_view(),name='create'),
             path('api/category/get/', views.ajax_get_category, name='ajax_get_category'),
             path('createcategory/',views.CreateCategoryView.as_view(),name='createcategory'),
             path('createparentcategory/',views.CreateParentCategoryView.as_view(),name='createparentcategory'),
             path('createstudents/',views.CreateStudentsView.as_view(),name='createstudents'),
             
             path('api/createstudent/get/',views.ajax_get_createstudent,name='ajax_get_createstudent'),
             path('typingselectstudent/',views.TypingSelectStudentView.as_view(),name='typingselectstudent'),
             
             path('api/deletestudents/get/',views.ajax_get_deletestudents,name='ajax_get_deletestudents'),
             path('api/studentslist/get/',views.ajax_get_studentslist,name='ajax_get_studentslist'),
             path('api/printlist/get/', views.ajax_get_printlist, name='ajax_get_printlist'),
             path('api/deleteparentcategory/get/', views.ajax_get_deleteparentcategory, name='ajax_get_deleteparentcategory'),
             path('api/createparentcategory/get/', views.ajax_get_createparentcategory, name='ajax_get_createparentcategory'),
             path('api/createcategory/get/', views.ajax_get_createcategory, name='ajax_get_createcategory'),
             path('api/deletecategory/get/', views.ajax_get_deletecategory, name='ajax_get_deletecategory'),
             path('api/createword/get/', views.ajax_get_createword, name='ajax_get_createword'),
             path('api/deleteword/get/', views.ajax_get_deleteword, name='ajax_get_deleteword'),
             path('api/saveuserscore/get/', views.ajax_get_saveuserscore, name='ajax_get_saveuserscore'),
             path('api/mypagelist/get/', views.ajax_get_mypagelist, name='ajax_get_mypagelist'),
             path('api/mypageparentlist/get/', views.ajax_get_mypageparentlist, name='ajax_get_mypageparentlist'),
]
