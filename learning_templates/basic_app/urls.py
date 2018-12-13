# pages/urls.py
from django.urls import path
from basic_app import views

#TEMPLATES TAGGING

app_name = 'basic_app'

urlpatterns = [

    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative_url_templates'),
    path('base/', views.base, name='base'),
]
