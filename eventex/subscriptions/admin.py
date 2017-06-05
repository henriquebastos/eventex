from django.contrib import admin
from eventex.subscriptions.models import Subscription


class SubscriptionModelAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'phone', 'cpf', 'created_at')
	date_hierarchy = 'created_at'


admin.site.register(Subscription, SubscriptionModelAdmin)
