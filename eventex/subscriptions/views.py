from django.contrib import messages
from django.conf import settings
from django.core import mail
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import FormMixin

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscriptionCreate(TemplateResponseMixin, FormMixin, View):
    template_name = 'subscriptions/subscription_form.html'
    form_class = SubscriptionForm

    def get(self, *args, **kwargs):
        self.object = None
        return self.render_to_response(self.get_context_data())

    def post(self, *args, **kwargs):
        self.object = None
        form = self.get_form()

        if not form.is_valid():
            return self.form_invalid(form)
        return self.form_valid(form)

    def form_valid(self, form):
        self.object = form.save()

        _send_mail('Confirmação de inscrição',
                   settings.DEFAULT_FROM_EMAIL,
                   self.object.email,
                   'subscriptions/subscription_email.txt',
                   {'subscription': self.object})

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return r('subscriptions:detail', self.object.pk)


new = SubscriptionCreate.as_view()

detail = DetailView.as_view(model=Subscription)


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])
