from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views.generic import ListView
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from .forms import EmailSendForm
# Create your views here.
from taggit.models import Tag
#using FBV
def post_list_view(request,tag_slug=None) :
   post_list=Post.objects.all()
   tag=None
   if tag_slug:
       tag=get_object_or_404(Tag,slug=tag_slug)
       post_list=post_list.filter(tags__in=[tag])
   paginator=Paginator(post_list,2)
   page_numer=request.GET.get('page')
   try :
       post_list=paginator.page(page_numer)
   except PageNotAnInteger:
       post_list=paginator.page(1)
   except EmptyPage:
       post_list=paginator.page(paginator.num_pages)
   return render(request,'BlogApp/post_list.html',{'post_list':post_list,'tag':tag})

from .forms import CommentForm
def post_detail_view(request,year,month,day,post) :
   post=get_object_or_404(Post,slug=post,
                          status='published',
                          publish__year=year,
                          publish__month=month,
                          publish__day=day,

                          )
   comments=post.comments.filter(active=True)
   new_comment=None
   csubmit=False
   if request.method=='POST' :
       form=CommentForm(request.POST)
       if form.is_valid():
           new_comment=form.save(commit=False)
           new_comment.post=post
           new_comment.save()
           csubmit=True
   else :
       form=CommentForm()

   return  render(request,'BlogApp/post_detail.html',{'post':post,'form':form,'csubmit':csubmit,'comments':comments})

#using CBV
# class PostListView(ListView):
#     model = Post
#     paginate_by = 1

def mail_send_view(request,id) :
  post=get_object_or_404(Post,id=id,status='published')
  form=EmailSendForm()
  return render(request,'BlogApp/sharebyemail.html',{'form':form,'post':post})
