from django.urls import path
from api.views import *

urlpatterns = [
    path("data/<type>", GetData.as_view()),
]