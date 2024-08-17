from django.urls import path
from .views import get_mark_list, get_model_list, search_parts, search_model

app_name = 'partfinder'

urlpatterns = [
    path('mark/', get_mark_list, name='mark'),
    path('model/', get_model_list, name='model'),
    path('search/part/', search_parts, name='search_part'),
    path('search/model/', search_model),
]
