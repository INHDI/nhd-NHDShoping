from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('home/',views.HomeView.as_view(),name='home' ),
    path('home/sanpham/<int:id>',views.loaisp,name='sanpham'),
    path('home/sanpham/chitiet/<int:id>',views.chitietsp),
    path('home/sanpham/chitiet/<int:Ten_sp>',views.chitietsp),
    path('home/addcart',views.addcart,name='muahang'),
    ]
