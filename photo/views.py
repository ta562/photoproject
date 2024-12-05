from django.shortcuts import render
from django.views.generic import TemplateView,ListView,View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import PhotoPostForm,EnglishWordsCreateForm,EnglishWordsTypingForm,CategoryCreateForm,ParentCategoryCreateForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import PhotoPost,EnglishWords,Category,ParentCategory
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views import generic
from django.http import JsonResponse # 追加


class IndexView(ListView):
    template_name='index.html'
    queryset=PhotoPost.objects.order_by('-posted_at')
    paginate_by=9

class CategoryView(ListView):
    template_name='index.html'
    paginata_by=9
    def get_queryset(self):
        category_id=self.kwargs['category']
        categories=PhotoPost.objects.filter(
            category=category_id).order_by('-posted_at')
        return categories

class DetailView(DetailView):
    template_name = 'detail.html'
    model=PhotoPost



class MypageView(ListView):
    template_name='mypage.html'
    paginate_by=9
    def get_queryset(self):
        queryset=PhotoPost.objects.filter(user=self.request.user).order_by('-posted_at')
        return queryset

class PhotoDeleteView(DeleteView):
    model=PhotoPost
    template_name='photo_delete.html'
    success_url=reverse_lazy('photo:mypage')
    def delete(self,request,*args,**kwargs):
        return super().delete(request,*args,**kwargs)
    
@method_decorator(login_required,name='dispatch')
class CreatePhotoView(CreateView):
    form_class=PhotoPostForm
    template_name="post_photo.html"
    success_url=reverse_lazy('photo:post_done')
    def form_valid(self,form):
        postdata=form.save(commit=False)
        postdata.user=self.request.user
        postdata.save()
        return super().form_valid(form)
# Create your views here.
class PostSuccessView(TemplateView):
    template_name='post_success.html'

class UserView(ListView):
    template_name='index.html'
    paginate_by=9
    def get_queryset(self):
        user_id=self.kwargs['user']
        user_list=PhotoPost.objects.filter(
            user=user_id).order_by('-posted_at')
        return user_list
    
class TypingView(generic.edit.CreateView):
    template_name='typing.html'
    model=EnglishWords
    form_class=EnglishWordsTypingForm
# getsucusessurl
# form_valid

    success_url=reverse_lazy('photo:create')
    def form_valid(self,form):
        form.instance.author=self.request.user
    # context
        return super(CreateView,self).form_valid(form)

class CreateView(LoginRequiredMixin,generic.edit.CreateView):
    model=EnglishWords
    template_name='createform.html'
    form_class=EnglishWordsCreateForm
    success_url=reverse_lazy('photo:create')
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super(CreateView,self).form_valid(form)
    
class CreateCategoryView(LoginRequiredMixin,TemplateView):
    model=Category
    template_name='createcategoryform.html'


class CreateParentCategoryView(LoginRequiredMixin,TemplateView):
    model=ParentCategory
    template_name='createparentcategoryform.html'
    

@csrf_exempt
def process(request):
    if request.method == 'POST':
        print('post')
        categorys=int(request.POST.get('categorys',0))
        english_text=list(EnglishWords.objects.filter(category=categorys).values_list('word', flat=True))
        trans_text=list(EnglishWords.objects.filter(category=categorys).values_list('trans', flat=True))
        category_text=list(Category.objects.filter(parent=categorys).values_list('title',flat=True))
        parentcategory_text=list(ParentCategory.objects.values_list('title',flat=True))
        data={'message':english_text,'message2':trans_text,'message3':category_text,'message4':parentcategory_text}
        return JsonResponse(data, json_dumps_params={'ensure_ascii':False})

def ajax_get_category(request):
    pk = request.GET.get('pk')
    # pkパラメータがない、もしくはpk=空文字列だった場合は全カテゴリを返す
    if not pk:
        category_list = Category.objects.all()
 
    # pkがあれば、そのpkでカテゴリを絞り込む
    else:
        category_list = Category.objects.filter(parent__pk=pk)
 
    # [ {'name': 'サッカー', 'pk': '3'}, {...}, {...} ] という感じのリストになる
    category_list = [{'pk': category.pk, 'title': category.title} for category in category_list]
 
    # JSONで返す
    return JsonResponse({'categoryList': category_list})
# modelsaveで保存してしまう

def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        category=Category.objects.values()        
        category_query_set=Category.objects.values_list('id')
        category_list=list(category_query_set)

        for i in category_list :
            context[i] =EnglishWords.objects.all().filter(category=i)

        context['category']=category
        context['category_list']=category_list
        return context

def ajax_get_createparentcategory(request):
        print('save')
        text = request.GET.get('title')
        obj=ParentCategory(title=text)
        obj.save()
        category_list = '保存'
        return JsonResponse({'categoryList': category_list})

def ajax_get_printlist(request):
        categorys = request.GET.get('pk')
        english_text=list(EnglishWords.objects.filter(category=categorys).values_list('word', flat=True))
        trans_text=list(EnglishWords.objects.filter(category=categorys).values_list('trans', flat=True))
        category_text=list(Category.objects.filter(parent=categorys).values_list('title',flat=True))
        category_id=list(Category.objects.filter(parent=categorys).values_list('id',flat=True))
        parentcategory_text=list(ParentCategory.objects.values_list('title',flat=True))
        parentcategory_id=list(ParentCategory.objects.values_list('id',flat=True))
    # [ {'name': 'サッカー', 'pk': '3'}, {...}, {...} ] という感じのリストになる
        data ={'message':english_text,'message2':trans_text,'message3':category_text,'message4':parentcategory_text,'message5':parentcategory_id,'message6':category_id}
    # JSONで返す
        return JsonResponse(data)
# modelsaveで保存してしまう


def ajax_get_deleteparentcategory(request):
        print('delete')
        text = request.GET.get('title')
        obj=ParentCategory.objects.filter(id=text)
        obj.delete()
        category_list = '削除'
        return JsonResponse({'categoryList': category_list})

def ajax_get_createcategory(request):
        print('save')
        text = request.GET.get('title')
        id = request.GET.get('parent')
        obj=Category(title=text,parent_id=id)
        obj.save()
        category_list = '保存'
        return JsonResponse({'categoryList': category_list})

def ajax_get_deletecategory(request):
        print('delete')
        text = request.GET.get('id')
        obj=Category.objects.filter(id=text)
        obj.delete()
        responsetext = '削除'
        return JsonResponse({'response': responsetext})