from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscriptionCreate(CreateView):
    model = Subscription
    form_class = SubscriptionForm
    email_to = None
    email_template_name = None

    def form_valid(self, form):
        response = super().form_valid(form)
        self.send_mail()
        return response

    def send_mail(self):
        subject = 'Confirmação de inscrição'
        from_ = settings.DEFAULT_FROM_EMAIL
        to = self.get_email_to()
        template_name = 'subscriptions/subscription_email.txt'
        context = self.get_email_context_data()

        body = render_to_string(template_name, context)
        mail.send_mail(subject, body, from_, [from_, to])

    def get_email_to(self):
        if self.email_to:
            return self.email_to
        return self.object.email

    def get_email_context_name(self):
        if self.email_context_name:
            return self.email_context_name
        return self.object._meta.model_name

    def get_email_context_data(self, **kwargs):
        context = dict(kwargs)
        context.setdefault(self.get_email_context_name(), self.object)
        return context


new = SubscriptionCreate.as_view()

detail = DetailView.as_view(model=Subscription)
