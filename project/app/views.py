from django.shortcuts import render, HttpResponse

# Create your views here.
def index(req):
    return render(req, "index.html")

def cls(r, s):
    return HttpResponse(s)

def custom_404(request, exception):
    return render(request, '404.html', status=404)
