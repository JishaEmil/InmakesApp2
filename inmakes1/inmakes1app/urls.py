
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('detail/', views.detail,name='detail'),
    path('thanks/', views.thanks,name='thanks'),
   path('passingvalue/', views.passingvalue,name='passingvalue'),
    path('page1/', views.page1, name='page1'),
    path('page1/resultpage/',views.resultpage,name='resultpage')
]