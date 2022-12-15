from django.urls import path

from .views import RatingAPIView

urlpatterns = [
    path(
        "rating_system", RatingAPIView.as_view(),
    ),
]
