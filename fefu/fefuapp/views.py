from django.http import HttpResponse
from .models import PostData
from django.views.decorators.csrf import csrf_exempt

def home_view(request):
    return HttpResponse("Hello, World!")

def about_view(request):
    return HttpResponse("О нас")

@csrf_exempt
def text_Post(request):
    if request.method == "POST":
        text = request.POST.get("text", "")
        if text:
            PostData.objects.create(text=text)
            return HttpResponse(f"<h1>Результат</h1><p>{text}</p>")
        return HttpResponse("<h1>Ошибка</h1><p>Поле 'text' не может быть пустым</p>")
    return HttpResponse("<h1>Ошибка</h1><p>Метод не поддерживается</p>")



