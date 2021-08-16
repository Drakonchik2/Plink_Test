from django.urls import path
from .views import CheckPar, ValParList

urlpatterns = [
    path('valpar/', CheckPar.as_view()),
    path('valparlist/', ValParList.as_view())
]