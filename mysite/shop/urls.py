
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index',views.index , name='index'),
    path('admin',views.admin , name='admin'),
    path('admin-Add-Jewellerys',views.admin_Add_Jewellerys , name='admin-Add-Jewellerys'),
    path('register',views.register , name='register'),
    path('login',views.handle_login,name='login'),
    path('logout',views.handle_logout,name='logout'),
    path('forgetpassword',views.forget_pass,name='forgetpassword'),
    path('contact',views.contact_us,name='contact'),
    path('about',views.about_us,name='about'),
    path('blog',views.blog,name='blog'),
    path('return-refund-replacement', views.return_refund_replacement, name='return-refund-replacement'),
    path('All-Jewellery-Sets', views.All_Jewellery_Sets, name='All-Jewellery-Sets'),
    path('Haram-Set', views.Haram_Set, name='Haram-Set'),
    path('Long-Necklace-Sets', views.Long_Necklace_Sets_fun, name='Long-Necklace-Sets'),
    path('Short-Necklace', views.Short_Necklace_fun, name='Short-Necklace'),
    path('Pendant-Sets', views.Pendant_Sets_fun, name='Pendant-Sets'),
    path('Mangalsutra-Sets', views.Mangalsutra_Sets_fun, name='Mangalsutra-Sets'),
    path('Earrings', views.Earrings_fun, name='Earrings'),
    path('Maang-Tikkas-And-Daminis', views.Maang_Tikkas_And_Daminis_fun, name='Maang-Tikkas-And-Daminis'),
    path('product/<title>', views.product),
    path('product/<int:id>/<title>', views.product),

]
