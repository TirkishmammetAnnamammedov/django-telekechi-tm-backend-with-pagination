from django.urls import include, path, re_path
from django.views.static import serve
from django.conf import settings
from .views import *

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^api/signup/users/$', sign_up, name='sign-up'),
    path('api/login/<str:user>/<str:password>', log_in, name='log-in'),
    path('api/islogin/<str:user>/<str:password>', is_login, name='is-logged-in'),
    path('api/login/<str:user>/<str:password>/<int:nm>', login_detail, name='login_detail'),
    re_path('api/forgotpasswords/$', forgot_passwords, name='forgot-passwords'),
    re_path(r'api/mainapi/$', turkmen_telekechi_main_api, name='mainapi'),
    re_path(r'^api/products/$', product_list, name='productapi'),
    path('api/newproducts/', new_product_api, name='newproducts' ),
    path('api/products/<int:nm>/', product_detail, name='detail'),
    re_path(r'^api/categories/$', category_list, name='categoryapi'),
    re_path(r'^api/products/search/$', search_products, name='searching-products'),
    re_path(r'^api/products/filter/$', filter_products, name='filtering-products'),
    path('api-auth/', include('rest_framework.urls'))
]
