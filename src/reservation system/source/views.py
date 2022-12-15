from collections import OrderedDict

import django_filters
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.renderers import JSONRenderer

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Reservation
from .serializers import ReservationSerializer


class Pagination(PageNumberPagination):
    page_size = None
    page_size_query_param = 'size'

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('total_elements', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('page', self.page.number),
            ('page_size', self.page.paginator.per_page),
            ('items', data)
        ]))


class ReservationView(ListCreateAPIView):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects
    renderer_classes = (JSONRenderer,)
    pagination_class = Pagination
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = "__all__"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            username=self.request.headers.get("X-User-Name")
        )
        return queryset

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            kwargs["data"]["username"] = self.request.headers.get("X-User-Name")
        return super().get_serializer(*args, **kwargs)


class ReservationUUIDView(RetrieveAPIView):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects
    renderer_classes = (JSONRenderer,)
    lookup_field = "reservation_uid"


class ReturnReservationView(UpdateAPIView):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects
    renderer_classes = (JSONRenderer,)
    lookup_field = "reservation_uid"
