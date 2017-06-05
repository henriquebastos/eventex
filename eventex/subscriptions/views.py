from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
	if request.method == 'POST':
		mail.send_mail('Confirmação de inscrição',
					   'Message',
					   'contato@eventex.com.br',
					   ['visitor@email.com'])

		return HttpResponseRedirect('/inscricao/')
	else:
		context = {'form': SubscriptionForm()}
		return render(request, 'subscriptions/subscription_form.html', context)
