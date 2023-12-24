from django.urls import path
from buildings.views import HouseViews

   
urlpatterns = [
    path("house", HouseViews.as_view(), name="index")
]

