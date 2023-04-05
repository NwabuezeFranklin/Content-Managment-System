from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('loginUser', views.loginUser, name='loginUser'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('registerUser', views.registerUser, name='registerUser'),
    path('profile/', views.profile, name='profile'),
    path('myProfile/<str:pk>', views.myProfile, name='myProfile'), 
    path('profileList/<str:pk>', views.profileList, name='profileList'),
    path('update/<str:pk>/', views.update, name='update'),
    path('uploads/<str:pk>/', views.uploads, name='uploads'), 
    path('comments/<str:pkm>/<str:pk>/<str:pkr>', views.comments, name='comments'),
    path('deleteProfile/<str:pk>/', views.deleteProfile, name='deleteProfile'),    
]


