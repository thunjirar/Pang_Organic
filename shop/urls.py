from django.urls import path
from . import views

# app_name = 'shop' # ถ้าใส่ตรงนี้ ใน template ต้องใช้ {% url 'shop:index' %}

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu_view, name='menu'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('custom/', views.custom_view, name='custom'),
    path('team/', views.team_view, name='team'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'), 

    path('admin-panel/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-panel/inventory/', views.inventory, name='inventory'),
    path('admin-panel/orders/', views.orders, name='orders'),
    path('admin-panel/shipping/', views.shipping, name='shipping'),
    path('admin-panel/customers/', views.customers, name='customers'),
    path('admin-panel/reports/', views.reports, name='reports'),
]

from django.conf import settings
from django.conf.urls.static import static

# ต่อท้าย urlpatterns เดิมของคุณ
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)