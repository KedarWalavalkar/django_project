from django.urls import path
from .import views
from itvedantapp1.models import Users,Category,Products
c=Category.objects.all()
urlpatterns = [
    # path('', admin.site.urls),
    path('', views.home, name='home'),
    # path('home.html', views.whileopening,{'c':c}),
    path('home.html',views.home,name='home'),
    path('adduser.html',views.adduser,name='adduser'),
    path('adduserdb',views.adduserdb),
    path('addcategorydb',views.addcategorydb),
    path('addproductdb',views.addproductdb),
    path('addproduct.html',views.addproduct,name='addproduct'),
    path('addcategory.html',views.addcategory,name='addcategory'),
    path('listusers.html',views.listusers,name='listusers'),
    path('Listcategory.html',views.Listcategory,name='Listcategory'),
    path('productlist.html',views.productlist,name='productlist'),
    path('deleteuser/<str:email>',views.deleteuser),
    path('deletecategory/<str:pro_category_name>',views.deletecategory),
    path('deleteproduct/<int:id>',views.deleteproduct),
    path('editproduct',views.editproduct),
    path('updateproduct',views.updateProduct),
    path('edituser',views.edituser),
    path('updateUser',views.updateUser),

    path('login',views.login),
    path('Loginto',views.Loginto),
    path('logout',views.delete_session),

    path('slist',views.slist),
    path('cart.html',views.cart),
    path('additemdb/<int:id>',views.additemdb),
    path('cart',views.cart),
    
    path('signup',views.signup),
    
]
