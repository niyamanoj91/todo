from django.urls import path
from .import views

urlpatterns = [
    path('',views.djann_create,name='home'),
    path('delete/<int:id>',views.delete_djann,name='delete_djann'),
    path('update/<int:id>',views.update_djann,name='update_djann')
]