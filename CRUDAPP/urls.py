
from django.urls import path
from . import views

app_name = 'crudapp'
urlpatterns = [

    # path('', views.index),
    path('', views.AddSearchCar, name="addsearchcar"),
    path('delete/<int:id>/', views.DeleteCar, name="deletecar"),
    path('update/<int:id>/', views.UpdateCar, name="updatecar"),
]