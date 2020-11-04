from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.list import MultipleObjectMixin

from eventex.core.models import Speaker, Talk, Course


class GenericHomeView(MultipleObjectMixin, TemplateView):
    pass


class HomeView(GenericHomeView):
    template_name = 'index.html'
    object_list = Speaker.objects.all()
    context_object_name = 'speakers'


def home(request):
    speakers = Speaker.objects.all()
    return render(request, 'index.html', {'speakers': speakers})


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'core/speaker_detail.html', {'speaker': speaker})


def talk_list(request):
    context = {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon(),
    }
    return render(request, 'core/talk_list.html', context=context)
