from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Hello, World!")

def about_view(request):
    return HttpResponse("О нас")