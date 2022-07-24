from django.urls import path
from . import views

urlpatterns = [
    path("stock/", views.GetStock.as_view()),
    path("crypto/", views.GetCrypto.as_view()),
]
