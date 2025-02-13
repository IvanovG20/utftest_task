from django.urls import path

from api.views import FoodListView


urlpatterns = [
    path('v1/foods/', FoodListView.as_view())
]
