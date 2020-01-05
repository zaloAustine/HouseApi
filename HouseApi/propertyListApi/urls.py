from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls import url
from .views import view_property_list,add_property_list,update_property,delete_property,Single_property

urlpatterns = [
    path('properties/',view_property_list),
    path('addproperties/', add_property_list),
    path('updateproperties/<int:pk>/', update_property),
    path('deleteproperties/<int:pk>/', delete_property),
    path('properties/<int:pk>/', Single_property),

]