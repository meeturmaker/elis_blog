
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect,Http404
from django.db.models import Q
from django.contrib import messages
from comments.forms import CommentForm
from comments.models import Comment

from .models import Post
from .forms import PostForm
# Create your views here.
def Posts(request):
  

  queryset = Post.objects.all()
  query = request.GET.get("q")
  if query:
	  queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(category__icontains=query)|
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query)| 
            Q(user__last_name__icontains=query)
        ).distinct()
  
  paginator = Paginator(queryset, 6)
  page_request_var = "page"
  page = request.GET.get(page_request_var)
  try:
    queryset = paginator.page(page)
  except PageNotAnInteger:
    queryset = paginator.page(1)
  except EmptyPage:
    queryset = paginator.page(paginator.num_pages)
    
  
  context = {
    
    "page_request_var": page_request_var,
    "posts": queryset, 
    }
  return render(request,"index.html",context)
  



def post_detail(request,slug=None):
  instance = get_object_or_404(Post, slug=slug)
  # if not request.user.is_staff or not request.user.is_superuser:
	# 		raise Http404
  # # work =Post.objects.filter(category="work") 
  post_cat = Post.objects.all()
  
  comments = Comment.objects.filter(instance=instance.id,parent=None)
  # initial_data = {
  #   "content_type":instance.get_content_type,
  #   "object_id":instance.id
  # }
  form = CommentForm(request.POST or None )
  if form.is_valid():
    # c_type = form.cleaned_data.get("content_type")
    # content_type = ContentType.objects.get(model=c_type)
    # obj_id = form.cleaned_data.get("object_id")
    content_data = form.cleaned_data.get("content")
    #this is just to ensure the parent_id obtained is aactually an integer
    parent_obj=None
    parent_id = request.POST.get("parent_id")
    if parent_id:
      parent_qs = Comment.objects.filter(id=parent_id)
      if parent_qs.exists() and parent_qs.count()==1:#just to ensure the filter parent_qs isnt messing up
        parent_obj = parent_qs.first()
    new_comment, created = Comment.objects.get_or_create(
                      user = request.user,
                      
                      # content_type = content_type,
                      # object_id = obj_id,
                      content = content_data,
                      instance =instance,
                      parent =parent_obj
                         )
                      
    return redirect(instance.get_absolute_url())
      
    if created:
      print("yeah")
  context ={
    "instance":instance,
    "comments":comments,
    "comment_form":form,
    
    "posts":post_cat
  }
  
  return render(request,"details.html",context)

      
  
  
  
  
def about(request):
  return render(request,"about.html")
    
  
   

  
  # initial_data = {
  #           "content_type": instance.get_content_type,
	#       		"object_id": instance.id
	#   }
	
  # form = CommentForm(request.POST or None, initial=initial_data)
  
  # if form.is_valid() and request.user.is_authenticated:
  #   c_type = form.cleaned_data.get("content_type")
  #   content_type = ContentType.objects.get(model__iexact=c_type)
  #   obj_id = form.cleaned_data.get("object_id")
	  
  #   content_data = form.cleaned_data.get("content")
	  
  #   parent_obj = None
  #   try:
	#     parent_id = int(request.POST.get("parent_id"))
	  
  #   except:
	#     parent_id = None

  #   if parent_id:
  #     parent_qs = Comment.objects.filter(id=parent_id)
  #     if parent_qs.exists() and parent_qs.count() == 1:
  #       parent_obj = parent_qs.first()
			 
    
  #   new_comment, created= Comment.objects.get_or_create(
  #                   user=request.user,
  #                   object_id=obj_id,
  #                   content_type=content_type,
  #                   content=content_data,
  #                   parent=parent_obj,
  #                     )
  #   if created:
  #     print("created")                
  #   return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

  

  # comments = Comment.objects.filter_by_instance(instance)
  # comments = instance.comments
  

    
  
  



def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
		
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url()) 
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)


def post_update(request,slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)	
  
	form = PostForm(request.POST or None, request.FILES or None,instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		# message success
		messages.success(request, "Successfully Updated")
		return HttpResponseRedirect(instance.get_absolute_url()) 
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)


def post_delete(request,slug=None):
  if not request.user.is_staff or not request.user.is_superuser:
    raise Http404
  instance = get_object_or_404(Post,slug=slug)
  instance.delete()
  messages.success(request,"Successfully deleted")
	
  return redirect("post")
