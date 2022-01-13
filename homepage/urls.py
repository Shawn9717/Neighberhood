from django.urls import path
from .views import PostCreateView,PostDetailView
from . import views
app_name = "homepage"
urlpatterns = [
    path("",views.index, name="index"),
    path('post/new/', PostCreateView.as_view(), name='new_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('join_hood/<int:pk>/', views.joinHood, name='join_hood'),
    path('delete_post/<int:pk>/', views.deletePost, name='delete_post'),
    path('create_business/<int:pk>/', views.createBusiness, name='create_business')
    #path('post/<int:pk>/', views.detailView,name="post-detail"),
]