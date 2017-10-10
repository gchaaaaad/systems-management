from django.shortcuts import render, get_object_or_404
from .models import System

def system_list(request):
    systems = System.objects.all()
    return render(request, 'systest/system_list.html',{'systems': systems})

def system_versions(request,pk):
    system_versions = get_object_or_404(Version, system_id = pk)
    return render(request, 'systest/system_versions.html', {'system_versions': system_versions})