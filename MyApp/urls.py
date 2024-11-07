from django.urls import path

from MyApp import views
urlpatterns = [
    path('', views.home, name='my_index'),
    path('services/', views.services, name='my_services'),
    path('about/', views.about, name='my_about'),
    path('blog/', views.blog, name='my_blog'),
    path('contacts/',views.contacts, name='my_contacts'),
]

