from eventex.subscriptions.views import new, detail
from django.urls import path

app_name = 'subscriptions'

urlpatterns = [
    path('inscricao/', new, name='new'),
    path('inscricao/<int:pk>/', detail, name='detail'),
]