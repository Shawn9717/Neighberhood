
from django.urls import path,include,re_path
from . import views
from django.contrib.auth import views as auth_views

app_name = "users"   


urlpatterns = [
    path('api/profile',views.ProfileList.as_view()),
    path('profile/',views.profile,name = 'profile'),
    #path('user_profile/',views.user_profile,name = 'user_profile'),
    path('edit_profile/',views.edit_profile,name = 'edit_profile'), 
    path("/", views.register, name="register"),
    #path('profile/',views.profile,name = 'profile'),

    

]