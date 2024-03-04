from django.urls import path
from . import views

# so basically give this app name as we are going to manage the urls which are connecting to 'items/' from here
# and also link this to the puddle urls so that we can handle the rest of item/ here
app_name = "item"
urlpatterns = [
    path('', views.items, name='items'),
    path('new/', views.new, name="new"),
    path('<int:pk>/', views.detail, name="detail"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/edit/', views.edit, name="edit")

]