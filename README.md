# Eventex

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/henriquebastos/eventex.svg?branch=master)](https://travis-ci.org/henriquebastos/eventex)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.6
3. Ative o virtualenv.
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:/henriquebastos/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envia as configurações para o heroku
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstancia

heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=.herokuapp.com

# Configure o email com sendgrid
heroku addons:create sendgrid:starter
heroku config:set EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
heroku config:set EMAIL_HOST_USER=`heroku config:get SENDGRID_USERNAME`
heroku config:set EMAIL_HOST_PASSWORD=`heroku config:get SENDGRID_PASSWORD`

git push heroku master --force
```
