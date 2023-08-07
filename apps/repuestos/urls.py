from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'repuestos'

urlpatterns = [
     path('',views.RepuestosForm.as_view(), name='create'),

]
