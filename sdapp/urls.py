from django.urls import path
from .import views


urlpatterns=[
    path('',views.indexpg,name='indexpg'),
    path('regist',views.regpage,name='regpage'),
    path('login',views.loginpage,name='loginpage'),
    path('about',views.aboutpg,name='aboutpg'),
    path('blog',views.blogpg,name='blogpg'),
    path('contact',views.contactpg,name='contactpg'),
    path('search',views.searchpg,name='searchpg'),

    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('shoping-cart',views.shopcart,name='shopcart'),
    path('logout_fn',views.logout_fn,name='logout_fn'),
    
    
    path('category',views.categorypg,name='categorypg'),
    path('<slug:slug>',views.category_products,name='category_products'),
    path('product/<slug:slug>',views.detail_page,name='detail_page'),
    path('pluscart/<int:cart_id>/',views.pluscart,name='pluscart'),
    path('minuscart/<int:cart_id>/',views.minuscart,name='minuscart'),
    path('deletecart/<int:cart_id>/',views.deletecart,name='deletecart')
    
   
]