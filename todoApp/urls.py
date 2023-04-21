from django.urls import path
from . import views

urlpatterns = [
    path('todos', views.get_all_task),
    path('todo/<int:pk>', views.get_a_task),

]
