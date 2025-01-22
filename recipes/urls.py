from django.urls import path
from . import views, auth_views

urlpatterns = [
    path('', views.recipes, name = 'recipes'),
    path('update-recipe/<slug:slug>/', views.update_recipe, name = 'update_recipe'),
    path('delete-recipe/<slug:slug>/', views.delete_recipe, name = 'delete_recipe'),
    path('login/', auth_views.login_page, name='login'),
    path('logout/', auth_views.logout_page, name='logout'),
    path('register/', auth_views.register, name='register'),
]