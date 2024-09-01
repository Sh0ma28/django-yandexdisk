from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    path = ''
    if request.method == 'POST':
        if request.POST.get('public_key'):
            key = request.POST.get('public_key')
        else:
            return render(request, 'app/index.html')
        if request.POST.get('path'):
            path = request.POST.get('path')
        r = requests.get(f'https://cloud-api.yandex.net/v1/disk/public/resources?public_key={key}&limit=100&path={path}')
        items = r.json().get('_embedded', {}).get('items', [])
        return render(request, 'app/index.html', {'data': items,
                                                  'name': r.json().get('name'),
                                                  'public_key': key,
                                                  'path': path})
    return render(request, 'app/index.html')