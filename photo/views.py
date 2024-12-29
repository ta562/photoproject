from django.shortcuts import render
from django.views.generic import TemplateView,ListView,View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import PhotoPostForm,EnglishWordsCreateForm,EnglishWordsTypingForm,CategoryCreateForm,ParentCategoryCreateForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import PhotoPost,EnglishWords,Category,ParentCategory,EnglishScore,Students
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views import generic
from django.http import JsonResponse # 追加


class IndexView(generic.edit.CreateView):
    template_name='typingpractice.html'
    model=EnglishWords
    form_class=EnglishWordsTypingForm

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
        queryset=EnglishScore.objects.filter(user=self.request.user)
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
    def get(self, request, **kwargs):
        name=Students.objects.values_list('name',flat=True).get(student_id=kwargs['pk'])
        context = {
            'pk': kwargs['pk'], 
            'name':name,        
        }
        return self.render_to_response(context)

class ScoreView(generic.edit.CreateView):
    template_name='score.html'
    model=EnglishWords
    form_class=EnglishWordsTypingForm
    def get(self, request, **kwargs):
        name=Students.objects.values_list('name',flat=True).get(student_id=kwargs['pk'])
        context = {
            'pk': kwargs['pk'], 
            'name':name,
           
        }

        return self.render_to_response(context)


class CreateStudentsView(LoginRequiredMixin,TemplateView):
     template_name='createstudents.html'
     login_url = reverse_lazy('index.html') 

class CreateDeleteStudentsView(LoginRequiredMixin,TemplateView):
     template_name='createdeletestudents.html'

class CreateView(LoginRequiredMixin,generic.edit.CreateView):
    model=EnglishWords
    template_name='createform.html'
    form_class=EnglishWordsCreateForm
    success_url=reverse_lazy('photo:create')
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super(CreateView,self).form_valid(form)

class CreateEditView(LoginRequiredMixin,TemplateView):
      template_name='createformedit.html'
      def get(self, request, **kwargs):
        context = {'id': kwargs['id'],'word':kwargs['word'],'trans':kwargs['trans']}
        return self.render_to_response(context)

class CreateCategoryView(LoginRequiredMixin,TemplateView):
    model=Category
    template_name='createcategoryform.html'

class EditCategoryView(LoginRequiredMixin,TemplateView):
      template_name='createcategoryedit.html'
      def get(self, request, **kwargs):
        context = {'id': kwargs['id'],'title':kwargs['title']}
        return self.render_to_response(context)

class CreateParentCategoryView(LoginRequiredMixin,TemplateView):
    model=ParentCategory
    template_name='createparentcategoryform.html'
    
class EditParentCategoryView(LoginRequiredMixin,TemplateView):
      template_name='createparentedit.html'
      def get(self, request, **kwargs):
        context = {'id': kwargs['id'],'title':kwargs['title']}
        return self.render_to_response(context)

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
        english_id=list(EnglishWords.objects.filter(category=categorys).values_list('id', flat=True))
        english_text=list(EnglishWords.objects.filter(category=categorys).values_list('word', flat=True))
        trans_text=list(EnglishWords.objects.filter(category=categorys).values_list('trans', flat=True))
        category_text=list(Category.objects.filter(parent=categorys).values_list('title',flat=True))
        category_id=list(Category.objects.filter(parent=categorys).values_list('id',flat=True))
        parentcategory_text=list(ParentCategory.objects.values_list('title',flat=True))
        parentcategory_id=list(ParentCategory.objects.values_list('id',flat=True))
       
      
    # [ {'name': 'サッカー', 'pk': '3'}, {...}, {...} ] という感じのリストになる
        data ={'message':english_text,'message2':trans_text,'message3':category_text,'message4':parentcategory_text,'message5':parentcategory_id,'message6':category_id,'message7':english_id,}
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

def ajax_get_createword(request):
        print('save')
        text1 = request.GET.get('word')
        text2 = request.GET.get('trans')
        id = request.GET.get('category')
        obj=EnglishWords(word=text1,trans=text2,category_id=id)
        obj.save()
        category_list = '保存'
        return JsonResponse({'categoryList': category_list})

def ajax_get_editword(request):
        print('save')
        text1 = request.GET.get('word')
        text2 = request.GET.get('trans')
        text3 = request.GET.get('id')
        format(text3)
        print(text1+text2)
        obj=EnglishWords.objects.get(id=text3)
        obj.word=text1
        obj.trans=text2
        obj.save()
        category_list = '保存'
        return JsonResponse({'categoryList': category_list})

def ajax_get_editer(request):
        print('save')
        text1 = request.GET.get('title')
        text2 = request.GET.get('id')
        text3 = request.GET.get('target')
        
        if text3=='category':
             categoryobj=Category.objects.get(id=text2)
             categoryobj.title=text1
             categoryobj.save()
        elif text3=='parent':
             parentobj=ParentCategory.objects.get(id=text2)
             parentobj.title=text1
             parentobj.save()    

        category_list = '保存'
        return JsonResponse({'categoryList': category_list})

def ajax_get_createwordcsv(request):
        
        text1 = request.GET.get('wordcsv')
        
        id = request.GET.get('category')
        print(id)
        print(text1)
        # for i in text1:
        #     splitword=i.split(',')
        #     print(splitword)
        #     obj=EnglishWords(word=splitword[0],trans=splitword[1],category_id=id)
        #     obj.save()

        category_list = '保存'
        return JsonResponse({'categoryList': category_list})

def ajax_get_deleteword(request):
        print('delete')
        text = request.GET.get('id')
        obj=EnglishWords.objects.filter(id=text)
        obj.delete()
        responsetext = '削除'
        return JsonResponse({'response': responsetext})

def ajax_get_saveuserscore(request):
        text1=request.GET.get('category')
        text2=request.GET.get('pk')
        text=Students.objects.get(student_id=text2)
        print(text1)
        print(text2)
        obj=EnglishScore(student_id=text.id,category_id=text1)
        obj.save()
        return JsonResponse({'response': text2})



def ajax_get_mypagelist(request):
        text=request.GET.get('pk')
        print(text)
        text1=Students.objects.get(student_id=text)
        text2=list(EnglishScore.objects.order_by('category_id__parent__id').filter(student_id=text1.id).values_list('category_id__parent__title',flat=True))
        print(text2)
        parents=list(set(text2))
        print(parents)
                  
        data ={'category':parents}
        return JsonResponse(data)



def ajax_get_mypagecategorylist(request):
        text=request.GET.get('category')
        text5=request.GET.get('pk')
        text4=Students.objects.get(student_id=text5)
        
        text2=list(EnglishScore.objects.filter(category_id__parent__title=text,student_id=text4.id).values_list('category_id__title',flat=True))
        print(text2)
        text3=list(set(text2))
        print(text3)
        number=[]
        for cate in text3:
            count=EnglishScore.objects.filter(category_id__title=cate,student_id=text4.id).count()
            number.append(count)   
        data ={'category':text3,'number':number}
        return JsonResponse(data)

def ajax_get_mypagecategorynumber(request):
        text=request.GET.get('category')
        text5=request.GET.get('pk')
        text4=Students.objects.get(student_id=text5)
        print(text)
       
        text2=EnglishScore.objects.filter(category_id__title=text,student_id=text4.id).count()
        data ={'number':text2}
        return JsonResponse(data)

def ajax_get_createstudent(request):
        print('save')
        text1 = request.GET.get('student_id')
        text2 = request.GET.get('student_name')
        text3 = request.GET.get('user_id')
       
        text3=request.user.id
        print(text1)
        print(text2)
        
        obj=Students(student_id=text1,name=text2,user_id=text3)
        obj.save()
        category_list = '保存'
        return JsonResponse({'categoryList': category_list})

def ajax_get_createstudentselect(request):
        print('save')
        text1 = request.GET.get('student_id')
        text2 = request.GET.get('student_name')
        text3 = request.GET.get('user_id')
       
        
        print(text1)
        print(text2)
        
        obj=Students(student_id=text1,name=text2,user_id=text3)
        obj.save()
        category_list = '保存'
        return JsonResponse({'categoryList': category_list})
def ajax_get_studentslist(request):
        
        pk=request.user.id
        print(pk)
             
        student_id=list(Students.objects.filter(user=pk).values_list('student_id', flat=True))
        student_name=list(Students.objects.filter(user=pk).values_list('name', flat=True))
        data ={'student_id':student_id,'student_name':student_name}
        return JsonResponse(data)

def ajax_get_studentslistselect(request):
        
        pk=request.GET.get('pk')
        print(pk)
             
        student_id=list(Students.objects.filter(user=pk).values_list('student_id', flat=True))
        student_name=list(Students.objects.filter(user=pk).values_list('name', flat=True))
        data ={'student_id':student_id,'student_name':student_name}
        return JsonResponse(data)

def ajax_get_deletestudents(request):
        print('delete')
        text = request.GET.get('student_id')
        obj=Students.objects.filter(student_id=text)
        obj.delete()
        responsetext = '削除'
        return JsonResponse({'response': responsetext})

class TypingSelectStudentView(LoginRequiredMixin,TemplateView):
    
    template_name='typingselectstudent.html'

def ajax_get_checkstudentslist(request):
        pk=request.GET.get('pk')
        print(pk)
        try:
             studentobj=Students.objects.get(student_id=pk)
             student_name=studentobj.name
        except:
             student_name='None'
        print(student_name)
        data ={'student':student_name}
        return JsonResponse(data)