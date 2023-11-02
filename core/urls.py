from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar/', views.buscar_productos, name='buscar_productos'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('admin_panel/create_user/', views.create_user, name='create_user'),
    path('admin_panel/delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('create_superuser/', views.create_superuser, name='create_superuser'),
    path('admin_panel/edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('product_panel/', views.product_panel, name='product_panel'),
    path('user_panel/', views.user_panel, name='user_panel'),
    path('product/create/', views.create_product, name='create_product'),
    path('product/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('product/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('product/detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('agregar-al-carrito/<int:product_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('modificar-cantidad/<int:cart_item_id>/', views.modificar_cantidad, name='modificar_cantidad'),
    path('eliminar-producto/<int:cart_item_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('carrito/', views.carrito, name='carrito'),
    path('acerca.html', views.acerca, name='acerca'),
    path('contacto.html', views.contacto, name='contacto'),
    path('faq.html', views.faq, name='faq'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
