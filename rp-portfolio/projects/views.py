from django.shortcuts import render
from django.shortcuts import get_object_or_404
from projects.models import Project

# Create your views here.
def project_index(request):
    return render(request,'project_index.html',{'projects':Project.objects.all()})

def project_detail(request,pk):
    project = get_object_or_404(Project,pk=pk)
    return render(request,'project_detail.html',{'project':project})

