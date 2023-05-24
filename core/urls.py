from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('cart/', cart, name='cart'),
    path('add/cart/<int:product_id>', add_to_cart, name='add-to-cart'),
    path('remove/cart/<int:cart_item_id>', remove_from_cart, name='remove-from-cart'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('account/', admin_home, name='dashboard'),
    path('account/login/', admin_login, name='admin-login'),
    path('account/logout/', logout_user, name='logout'),
    path('account/add/product', add_product, name='add-product'),
    path('account/edit/product/<str:pk>', edit_product, name='edit-product'),
    path('account/delete/product/<str:pk>', delete_product, name='delete-product'),
]
