from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
	if request.method == 'POST':
		return create(request)
	else:
		return new(request)


def create(request):
	form = SubscriptionForm(request.POST)

	if not form.is_valid():
		return render(request, 'subscriptions/subscription_form.html',
			          {'form': form})

	body = render_to_string('subscriptions/subscription_email.txt',
		                     form.cleaned_data)

	mail.send_mail('Confirmação de inscrição',
				   body,
				   'contato@eventex.com.br',
				   ['contato@eventex.com.br', form.cleaned_data['email']])

	messages.success(request, 'Inscrição realizada com sucesso!')

	return HttpResponseRedirect('/inscricao/')


def new(request):
	return render(request, 'subscriptions/subscription_form.html',
		          {'form': SubscriptionForm()})
