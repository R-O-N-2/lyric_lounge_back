from django.urls import path 
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('user/', views.UserList.as_view(), name='user_list'),
    path('work/', views.WorkList.as_view(), name="work_list"),
    path('user/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('work/<int:pk>', views.WorkDetail.as_view(), name="work_detail"),
    path('genre/', views.GenreList.as_view(), name='genre_list'),
    path('genre/<int:pk>', views.GenreDetail.as_view(), name='genre_detail'),
    path('alias/', views.AliasList.as_view(), name='alias_list'),
    path('alias/<str:name>', views.AliasDetail.as_view(), name='alias_detail')
]