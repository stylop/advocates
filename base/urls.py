from django.urls import path
from .views import AdvocateListView, AdvocateDetailAPIView

urlpatterns = [
    path('advocates/', AdvocateListView.as_view()),
    path('advocates/<str:username>/', AdvocateDetailAPIView.as_view()),

]