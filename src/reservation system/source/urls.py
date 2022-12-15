from django.urls import path

from .views import ReservationView, ReservationUUIDView, ReturnReservationView

urlpatterns = [
    path(
        "reservations", ReservationView.as_view(),
    ), path(
        "reservations/<uuid:reservation_uid>/", ReservationUUIDView.as_view(),
    ), path(
        "reservations/<uuid:reservation_uid>/return", ReturnReservationView.as_view(),
    ),
]
