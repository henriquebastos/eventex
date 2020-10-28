from eventex.subscriptions.views import subscribe, detail
from django.urls import path

urlpatterns = [
    path('inscricao/', subscribe),
    path('inscricao/<int:pk>/', detail),
]