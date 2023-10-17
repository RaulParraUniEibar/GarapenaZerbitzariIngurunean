from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name = 'Index'),
    path('add/', views.add, name='add'),
    path('add/addcasa/',views.addcasa,name='addcasa'), 
    path('add/addpersona/',views.addpersona,name='addpersona'),
    path('add/addalquiler/',views.addalquiler,name='addalquiler'),
    path ('eliminarcasa/<int:id>/', views.deletecasa, name='deletecasa'),
    path ('eliminarpersona/<int:id>/', views.deletepersona, name='deletepersona'),
    path ('eliminaralquiler/<int:id>/', views.deletealquiler, name='deletealquiler'),
    path ('updatepersona/<int:id>/', views.updatepersona, name='updatepersona'),
    path ('editarpersona/<int:id>/', views.editarpersona, name='editarpersona'),
    path ('updatecasa/<int:id>/', views.updatecasa, name='updatecasa'),
    path ('editarcasa/<int:id>/', views.editarcasa, name='editarcasa'),
]