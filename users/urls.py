from django.urls import path
from .views import *

urlpatterns = [
    
    path('upload', upload_data, name='upload_data'),
    path('query-builder', query_builder_data_show, name='query_builder'),
    path('filtered-data-count', filtered_data_count_api, name='filtered_data_count'),

    path('users', user_list, name='user_list'),
    path('add-user', add_user, name='add_user'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
]
