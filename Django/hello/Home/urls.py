from django.contrib import admin
from django.urls import path
from Home import views

admin.site.site_header = "Amul Ice Cream Admin"
admin.site.site_title = "Amul Ice Cream Admin Portal"
admin.site.index_title = "Welcome to Amul Ice Cream Portal"

urlpatterns = [
    path('',views.index, name="home"),
    path('about/',views.about, name="about"),
    path('services/',views.services, name="services"),
    path('contact/',views.contact, name="contact")
]
