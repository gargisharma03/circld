from django.urls import path
from .views import ProfileView, EmailTokenObtainPairView

urlpatterns = [
    path('profile/', ProfileView.as_view()),
    path('token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
