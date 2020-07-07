from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clothings/', views.clothings_index, name='index'),
    path('myclothings/', views.myclothings_index, name='myindex'),
    path('clothings/<int:clothing_id>/', views.clothings_detail,
         name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('clothings/create/',
         views.ClothingCreate.as_view(),
         name='clothings_create'),
    path('clothings/<int:pk>/update/',
         views.ClothingUpdate.as_view(),
         name='clothings_update'),
    path('clothings/<int:pk>/delete/',
         views.ClothingDelete.as_view(),
         name='clothings_delete'),
    path('shoes/', views.ShoeList.as_view(), name='shoes_list'),
    path('shoes/<int:pk>', views.ShoeDetail.as_view(), name='shoes_detail'),
    path('shoes/create/', views.ShoeCreate.as_view(), name='shoes_create'),
    path('shoes/<int:pk>/update/',
         views.ShoeUpdate.as_view(),
         name='shoes_update'),
    path('shoes/<int:pk>/delete/',
         views.ShoeDelete.as_view(),
         name='shoes_delete'),
]
