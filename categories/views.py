from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from posts.models import Post
from django.db.models import Q

# Create your views here.
def family(request):
  queryset = Post.objects.filter(category="family")
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
    "category":queryset
  }
  return render(request,"family.html",context)


def lifestyle(request):
  
  queryset = Post.objects.filter(category="lifestyle")
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
    "category":queryset
  }
  return render(request,"lifestyle.html",context)


def health(request):
  
  queryset = Post.objects.filter(category="health")
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
    "category":queryset
  }
  return render(request,"health.html",context)


def management(request):
  
  queryset = Post.objects.filter(category="management")
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
      "category": queryset
  }
  return render(request,"management.html",context)


def travel(request):
  
  queryset = Post.objects.filter(category="travel")
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
    "category": queryset
  }
  return render(request,"travel.html",context)


def fashion(request):
  
  queryset = Post.objects.filter(category="fashion")
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
    "category":queryset
  }
  return render(request,"fashion.html",context)
