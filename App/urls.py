from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),

    path('loginUser', views.loginUser, name='loginUser'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('registerUser', views.registerUser, name='registerUser'),
    path('profile/', views.profile, name='profile'),
    path('myProfile/<str:pk>', views.myProfile, name='myProfile'), 
    path('profileList/<str:pk>', views.profileList, name='profileList'),
    path('guestProfile', views.guestProfile, name='guestProfile'),
    path('updateMe/<str:pk>/', views.updateMe, name='updateMe'),
    
    path('update/<str:pk>/', views.update, name='update'),
    path('updatePost/<str:pkm>/<str:pk>/<str:pkr>', views.updatePost, name='updatePost'),
    
    path('uploads/<str:pk>/', views.uploads, name='uploads'), 
    path('comments/<str:pkm>/<str:pk>/<str:pkr>', views.comments, name='comments'),
    path('deleteProfile/<str:pk>/', views.deleteProfile, name='deleteProfile'),    
    path('deletePost/<str:pkm>/<str:pk>/<str:pkr>', views.deletePost, name='deletePost'),    
    
]

handler404 = 'App.views.error'
