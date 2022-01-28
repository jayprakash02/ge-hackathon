from django.urls import path,include
from .views import VerifyingUser,UserViewSet

urlpatterns = [
    
    path('verify/',VerifyingUser.as_view(),name="Verifying User"),
    path('register/',UserViewSet.as_view({'post': 'create'}),name="Register User"),
]


