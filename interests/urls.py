from django.urls import path
from . import views

urlpatterns = [
    # Example endpoints for interests
    path('', views.InterestListView.as_view(), name='interest-list'),
    path('<int:pk>/', views.InterestDetailView.as_view(), name='interest-detail'),
]
