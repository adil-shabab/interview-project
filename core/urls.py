from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('account/', admin_home, name='dashboard'),
    path('account/login', admin_login, name='admin-login'),
    path('account/add/product', add_product, name='add-product'),
]
