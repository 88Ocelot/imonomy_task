from django.shortcuts import render
from render.models import ApiData


def render_apidata(request):
    data = ApiData.objects.all()
    return render(request, 'index.html', {'data': data})
