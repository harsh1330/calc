from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def submit(request):
    q= request.POST['query']
    try:
        ans= eval(q)
        thedict= {
            'q': q,
            'ans': ans,
            'error': False
        }
        return render(request, 'index.html', context= thedict)
    except:
        thedict= {
            'error': True
        }
        return render(request, 'index.html', context= thedict)