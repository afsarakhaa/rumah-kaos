from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
from main.views import register, login_user, logout_user
from . import views

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('tambah_amount/<int:product_id>/', views.tambah_amount, name='tambah_amount'),
    path('kurang_amount/<int:product_id>/', views.kurang_amount, name='kurang_amount'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),

]