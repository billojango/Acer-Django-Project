
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.aboutus, name='about'),
    path('contact/', views.contactus, name='contact'),
    path('table/', views.tableview, name='table'),
]
