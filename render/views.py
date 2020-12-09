from django.shortcuts import render
from render.models import ApiData


def render_apidata(request):
    cname_filter = request.GET.get('client_name', None)
    date_filter = request.GET.get('date', None)
    data = ApiData.objects.all()
    if cname_filter:
        data = data.filter(client_name=cname_filter)
    if cname_filter:
        data = data.filter(date=date_filter)
    return render(request, 'index.html', {'data': data})
