from django import forms


class SubscriptionForm(forms.Form):
	name = forms.CharField()
	cpf = forms.CharField()
	email = forms.EmailField()
	phone = forms.CharField()
