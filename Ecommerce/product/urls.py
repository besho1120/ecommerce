from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.home,name="home"),
    path('category/<int:categoryid>/',views.Category,name="Category"),
    path('product/<int:productid>/',views.Product,name="Product"),
    path('newproducts/',views.newproducts,name="newproducts"),
    path('checkout/', views.checkout, name='checkout'),
    path('addcart/<int:proid>/', views.addcart, name='addcarts'),
    path('cart/', views.cart, name='cart'),
    path('deleteitem/<int:proid>/', views.deleteitem, name='delete'),
]
