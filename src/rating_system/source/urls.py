from django.urls import path

from .views import RatingView

urlpatterns = [
    path(
        "rating_system", RatingView.as_view(),
    ),
]
