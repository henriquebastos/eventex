from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView

from eventex.core.models import Speaker, Talk

home = ListView.as_view(template_name='index.html',
                        model=Speaker)


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'core/speaker_detail.html', {'speaker': speaker})


talk_list = ListView.as_view(model=Talk)
