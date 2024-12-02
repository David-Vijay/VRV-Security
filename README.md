# This is a sample web application of Admin Dashboard for managing users, roles and permissions.

  Prerequisites:
  
  1. Python and Django: Ensure you have Python installed on your system. You can install Django using pip:
     pip install django
  2. Database: By default, Django uses SQLite, but you can configure it to use other databases like PostgreSQL, MySQL, or Oracle.
  3. Text Editor or IDE: Visual Studio code (recommended)

  Setting up Django project:
  
  To create a new Django project use below commands on a terminal.
  
    django-admin startproject vrv
    cd vrv
    python manage.py startapp app
  
  I have created a new project named 'vrv' and an app named "App"Application Registration: you need to configure in your settings.py file
      INSTALLED_APPS = [
          # ...
          'APP',
      ]
  
  Defining Models
  In Django, models are Python classes that define the structure of your database tables. For our project, let's assume we want to manage a list of users. Create a model for the users in app/models.py:
  from django.db import models
  
  # Create your models here.
      class crud(models.Model):
          username= models.CharField( max_length=50, null=False, blank=False)
          role = models.CharField(max_length=50)
          permission=models.CharField(max_length=50)
          status=models.CharField(max_length=50,)
          def __str__(self):
              return self.username
  Now, I've created the database tables for our models. Run the following commands to create the migrations and apply them:
  python manage.py makemigrations
  python manage.py migrate
  
  Creating Function-Based Views
  Function-based views are a simple and straightforward way to handle crud operations in Django. In this example, we'll create views for creating, reading, updating, and deleting user details.
  1. create a user in app/views.py:
     
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
       
  In this view, we handle both GET and POST requests. If it's a GET request, we render a form for creating a new order. If it's a POST request, we validate the form data and save the new order if it's valid
  2. read all the data passed to database and renders them using template
  
       def index(request):
        data=crud.objects.all()
        context={'data':data}
        return render(request,'index.html',context)
      
  3. To update the data:
  
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
  5. To Delete data:
     
         def delete(request,id):
          data=crud.objects.get(id=id)
          data.delete()
          messages.warning(request,'Data has been deleted successfully')
          return redirect('index')
          context={'data':data}
          return render(request,'index.html',context)
     
  Now, create HTML templates for the views in the VRV/templates directory. You'll need templates for the following views:
     1. Index.html --> the home page with user information.
  
            <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
          <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
          <title>Dashboard</title>
      </head>
      <body>
          <nav class="navbar navbar-dark bg-dark">
              <div class="container-md text-center">
                <a class="navbar-brand" href="#" class="text-center">Admin Dashboard</a>
              </div>
            </nav>  
          <div class="container mt-3">
                  <div class="col-md-4"></div>
                  <div class="col-md-12">
                      <div class="row">
                          <h2 class="text-center bg-dark text-white " >User Information</h2>
                          {% for message in messages %}
                          <div class="alert alert-{{message.tags}} alert-dismissible fade show" role="alert">
                            <strong>{{message}}</strong>
                            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                          {% endfor %}
                          </div>
                          <table class="table table-white table-hover">
                              <thead>
                                  <tr>
                                    <th scope="col">Username</th>
                                    <th scope="col">Role</th>
                                    <th scope="col">Permission</th>
                                    <th scope="col">Status</th>
                                    <th scope="col">Edit</th>
                                    <th scope="col">Delete</th>
                                  </tr>
                                </thead>
                                <tbody>
                                  {% for i in data%}
                                    <tr>
                                      <td>{{i.username}}</td>
                                      <td>{{i.role}}</td>
                                      <td>{{i.permission}}</td>
                                      <td>{{i.status}}</td>
                                      <td><a type="button" href='update/{{i.id}}' class="btn btn-outline-success">Edit</a></td>
                                      <td><a type="button" href="delete/{{i.id}}" class="btn btn-outline-danger">Delete</a></td>
                                    </tr>
                                  {% endfor %}
                                  </tbody>
                            </table>
                  </div>
      
                  <div class="text-center d-grid gap-4">
                      <a href="{% url 'adduser' %}" class="text-center  gap-2" style="text-decoration: none;"><button type="submit" class="btn btn-success mt-2">Add User</button></a>
                  </div>
                  <div class="col-md-12"></div>
                      </div>
                  
              </div>
          </div>    
      </body>
      </html>
  
     2. add.html --> the details will be added from this page.
  
            <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
          <title>adduser</title>
      </head>
      <body>
          <nav class="navbar navbar-dark bg-dark">
              <div class="container-md text-center">
                <a class="navbar-brand" href="#" class="text-center">Admin Dashboard</a>
              </div>
            </nav>  
          <div class="container mt-4">
              <div class="row">
                  <div class="col-md-3">
                  </div>
                  <div class="col-md-6" >
                      <h2 class="text-center bg-dark text-white" >Add User</h2>
                  
                          <form method="post">
                              {% csrf_token %}
                              <div class="form-group">
                                <label for="Username">Username</label>
                                <input type="text" class="form-control mt-2" id="username"  placeholder="Username" name="username" required>
                              </div>
      
                              <div class="form-group">
                                <label for="Role" class="mt-2">Role</label>
                                <select class="form-control mt-2" id="exampleFormControlSelect1" name="role">
                                  <option>Admin</option>
                                  <option>User</option>
                                  <option>Developer</option>
                                </select>                
                              </div>
      
                              <div class="form-group">
                                  <label for="Permissions" class="mt-2">Permissions</label>
                                  <select class="form-control mt-2" id="exampleFormControlSelect1" name="permissions">
                                    <option>All</option>
                                    <option>Edit/view</option>
                                    <option>View only</option>
                                    <option>Update/Edit</option>
                                  </select>                
                                </div>
                                <div class="form-group">
                                  <label for="status" class="mt-2">Status</label>
                                  <select class="form-control mt-2" id="status" name="status">
                                    <option>Active</option>
                                    <option>Inactive</option> 
                                  </select>                
                                </div>
          
                                  <div class="text-center d-grid gap-4    ">
                                      <button type="submit" class="btn btn-success mt-2">Add</button>
                                  </div>
                            </form>
                      </div>
                  </div>
      
                  
                  
              </div>
          </div>    
      </body>
      </html>
      
    3. edit.html --> this is the page where the data is updated
  
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
          <title>adduser</title>
      </head>
      <body>
          <nav class="navbar navbar-dark bg-dark">
              <div class="container-md text-center">
                <a class="navbar-brand" href="#" class="text-center">Admin Dashboard</a>
              </div>
            </nav>  
          <div class="container mt-4">
              <div class="row">
                  <div class="col-md-3">
                  </div>
                  <div class="col-md-6" >
                      <h2 class="text-center bg-dark text-white" >Update User</h2>
                          <form method="post" action='/update/{{data.id}}'>    
                              {% csrf_token %}
                              <div class="form-group">
                                <label for="Username">Username</label>
                                <input type="text"  class="form-control mt-2" id="username"  placeholder="Username" name="username" required value={{data.username}}>
                              </div>
      
                              <div class="form-group">
                                <label for="Role" class="mt-2">Role</label>
                                <select class="form-control mt-2" id="exampleFormControlSelect1" name="role" value={{data.role}}>
                                  <option>Admin</option>
                                  <option>User</option>
                                  <option>Developer</option>
                                  
      
                                </select>                
                              </div>
      
                              <div class="form-group">
                                  <label for="Permissions" class="mt-2">Permission</label>
                                  <select class="form-control mt-2" id="exampleFormControlSelect1" name="permissions" value={{data.permission}}>
                                    <option>All</option>
                                    <option>Edit/view</option>
                                    <option>View only</option>
                                    <option>Update/Edit</option>
                                  </select>                
                                </div>
                                <div class="form-group">
                                  <label for="status" class="mt-2">Status</label>
                                  <select class="form-control mt-2" id="status" name="status">
                                    <option>Active</option>
                                    <option>Inactive</option> 
                                  </select>                
                                </div>
                                  <div class="text-center d-grid gap-4    ">
                                      <button type="submit" class="btn btn-success mt-2">update</button>
                                  </div>
                            </form>
                      </div>
                  </div>
      
                  
                  
              </div>
          </div>    
      </body>
      </html>
  
  Wiring Up URLs
  Finally, configure the URLs for your views. In your project's vrv/urls.py file, include the URLs for the app:
  
  from django.contrib import admin
  from django.urls import path, include
  
      urlpatterns = [
          path('admin/', admin.site.urls),
          path('', include('app.urls'))
      ]
  Then, in your app's aoo/urls.py file, define the URLs for your views:
  
      from django.urls import path
      from . import views
      from django.urls import path
      from app import views
      urlpatterns = [
          path('',views.index, name='index'),
          path('adduser/',views.add, name='adduser'),
          path('update/<id>',views.update, name= 'updatedata'),
          path('delete/<id>',views.delete, name= 'deletedata')
      ]
      
  Testing Your CRUD Project
  With everything set up, we can start your Django development server:
  
      python manage.py runserver
  
  Visit http://localhost:8000/ in your browser, and you should be able to create, read, update, and delete orders in Django using function-based views.
