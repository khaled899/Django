from django.urls import path
from .views import  PageView, get_all_pages, get_page,get_pages


urlpatterns = [
    path('pages/',get_pages),
    path('get-pages/',get_all_pages),
    path('<int:page_id>/',get_page),
    path('pages_serializer/',PageView.as_view()), 
    path('pages_serializer/<int:page_id>/',PageView.as_view())


]
