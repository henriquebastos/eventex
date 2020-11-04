from django.conf import settings
from django.core import mail
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.generic import DetailView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import ModelFormMixin, ProcessFormView

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscriptionCreate(TemplateResponseMixin, ModelFormMixin, ProcessFormView):
    template_name = 'subscriptions/subscription_form.html'
    form_class = SubscriptionForm

    def get(self, *args, **kwargs):
        self.object = None
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        self.object = None
        return super().post(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()

        _send_mail('Confirmação de inscrição',
                   settings.DEFAULT_FROM_EMAIL,
                   self.object.email,
                   'subscriptions/subscription_email.txt',
                   {'subscription': self.object})

        return HttpResponseRedirect(self.get_success_url())


new = SubscriptionCreate.as_view()

detail = DetailView.as_view(model=Subscription)


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])
