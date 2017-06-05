from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
	if request.method == 'POST':
		mail.send_mail('Confirmação de inscrição',
					   MESSAGE,
					   'contato@eventex.com.br',
					   ['contato@eventex.com.br', 'henrique@bastos.net'])

		return HttpResponseRedirect('/inscricao/')
	else:
		context = {'form': SubscriptionForm()}
		return render(request, 'subscriptions/subscription_form.html', context)


MESSAGE = """
Olá! Tudo bem?

Muito obrigada por se inscrever no Eventex.

Estes foram os dados que você nos forneceu
em sua inscrição:

Nome: Henrique Bastos
CPF: 12345678901
Email: henrique@bastos.net
Telefone: 21-99618-6180

Em até 48 horas úteis, a nossa equipe entrará
em contato com vocie para concluirmos a sua
matrícula.

Atenciosamente,
--
Morena
"""
