from django.urls import path

from . import views

urlpatterns = [
    path('', views.Posts, name='post'),
    path('about/', views.about, name='about'),
    path('create/', views.post_create, name='create'),
    path('<str:slug>/update/', views.post_update, name='update'),
    path('<str:slug>/delete/', views.post_delete, name='delete'),
    path('<str:slug>/', views.post_detail, name="detail"),
    ]

# urlpatterns = [
#     url(r'^$', post_list, name='list'),
#     url(r'^create/$', post_create),

#     url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
#     url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
#     #url(r'^posts/$', "<appname>.views.<function_name>"),
# ]
