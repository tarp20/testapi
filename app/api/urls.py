from django.urls import path

from .views import CarViewSet


urlpatterns = [
    path('car', CarViewSet.as_view({'post': 'create',
                                    'get': 'list'})),
    path('car/<int:pk>', CarViewSet.as_view({'get': 'retrieve'}))
]
