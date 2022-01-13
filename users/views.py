
from django.contrib.auth import login
from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse,reverse_lazy
from users.forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_protect
from .forms import UserUpdateForm,UpdateUserProfileForm
from django.contrib.auth.decorators import login_required 
from .models import Profile
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer
from django.contrib.auth.models import User
import users.signals
@csrf_protect
def register(request):
    context = {}
    form = CustomUserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'home/index.html')
    context['form']=form
    return render(request,'registration/register.html',context)
@login_required
def profile(request):
    """[Profile]

    Args:
        request ([get]): [http method to retrieve data]
        id ([profile]): [retrieve specified user profile]

    Returns:
        [type]: [description]
    """
    prof = Profile.objects.all()
    return render(request,'profile/profile.html', {"profile": prof})


def edit_profile(request):
    
    user= request.user
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user.profile)
        profile = Profile.objects.get(user = request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('users:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        #profile = Profile.objects.get(user = request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form
    }
    return render(request, 'profile/edit_profile.html', params)



# Update it here



class ProfileList(APIView):
    def get(self,request,format = None):
        all_profile = Profile.objects.all()
        serializerdata = ProfileSerializer(all_profile,many = True)
        return Response(serializerdata.data)
