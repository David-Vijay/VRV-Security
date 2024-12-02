from django.shortcuts import render,redirect
from .models import crud
from django.contrib import messages
# Create your views here.
def index(request):
    data=crud.objects.all()
    context={'data':data}
    return render(request,'index.html',context)

def add(request):
    if request.method=='POST':
        username= request.POST.get('username')
        role = request.POST.get('role')
        permissions = request.POST.get('permissions')
        status= request.POST.get('status')
        crud(username=username, role=role, permission=permissions,status=status).save()
        messages.success(request,'Data added successfully')
        return redirect('index')
    return render(request,'add.html')

def update(request,id):
    if request.method=='POST':
        username= request.POST['username']
        role = request.POST['role']
        permission= request.POST['permissions']
        status= request.POST['status']
        edit=crud.objects.get(id=id)
        edit.username=username
        edit.role=role
        edit.permission=permission
        edit.status=status
        edit.save()
        messages.success(request,'Data has been updated successfully')  
        return redirect('index')

    data=crud.objects.get(id=id)
    context={'data':data}
    return render(request,'edit.html',context)

def delete(request,id):
    data=crud.objects.get(id=id)
    data.delete()
    messages.warning(request,'Data has been deleted successfully')
    return redirect('index')
    context={'data':data}
     
    return render(request,'index.html',context)
    