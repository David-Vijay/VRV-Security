from django.urls import path
from app import views
urlpatterns = [
    
    path('',views.index, name='index'),
    path('adduser/',views.add, name='adduser'),
    path('update/<id>',views.update, name= 'updatedata'),
    path('delete/<id>',views.delete, name= 'deletedata')

    

]
