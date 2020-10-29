from django.shortcuts import render
from eventex.core.models import Speaker

def home(request):
	speakers = [
		{'name': 'Grace Hopper', 'photo': 'http://hbn.link/hopper-pic'},
		{'name': 'Alan Turing', 'photo': 'http://hbn.link/turing-pic'},
	]
	return render(request, 'index.html', {'speakers': speakers})


def speaker_detail(request, slug):
	speaker = Speaker(
		name='Grace Hopper',
		slug='grace-hopper',
		photo='http://hbn.link/hopper-pic',
		website='http://hbn.link/hopper-site',
		description='Programadora e almirante.',
	)
	return render(request, 'core/speaker_detail.html', {'speaker': speaker})

