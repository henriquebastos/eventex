from eventex.subscriptions.views import new, detail
from django.urls import path

app_name = 'subscriptions'

urlpatterns = [
    path('', new, name='new'),
    path('<int:pk>/', detail, name='detail'),
]