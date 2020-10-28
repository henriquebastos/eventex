from eventex.subscriptions.views import subscribe, detail
from django.urls import path

app_name = 'subscriptions'

urlpatterns = [
    path('inscricao/', subscribe, name='new'),
    path('inscricao/<int:pk>/', detail, name='detail'),
]