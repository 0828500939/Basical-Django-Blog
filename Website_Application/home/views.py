from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"pages/home.html")
def contact(request):
    return render(request, "pages/contact.html")
def error(request, exception=None):
    if exception is None:  # Xử lý lỗi 404
        return render(request, 'pages/error.html', status=404)
    else:  # Xử lý lỗi 500
        return render(request, 'pages/error.html', {'message': exception}, status=500)
