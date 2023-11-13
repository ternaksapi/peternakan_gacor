from django.urls import path
from main.views import show_main, create_items, show_xml, show_json, show_xml_with_id, show_json_by_id, register, login_user, logout_user, add_item_ajax, get_item_json

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-items', create_items, name='create_items'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', show_xml_with_id, name='show_xml_with_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-ajax/', add_item_ajax, name='add_item_ajax')
]