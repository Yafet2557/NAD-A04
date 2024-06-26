from django.shortcuts import render
from .models import Profile
from django.http import JsonResponse
from .forms import ProfileForm

# Create your views here.

def my_profile_view(request):
    obj = Profile.objects.get(user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=obj)
    
    if is_ajax(request):
        if form.is_valid():
            instance = form.save()
            return JsonResponse({
                'bio': instance.bio,
                'avatar': instance.avatar.url,
                'user':instance.user.username,
            })
    context = {
        'obj':obj,
        'form':form,
    }
    
    return render(request, 'profiles/main.html', context)
    
    
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'