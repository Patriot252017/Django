from django.shortcuts import render, redirect
from .models import PostData


def post_list_and_create(request):
    if request.method == "POST":
        text = request.POST.get("text", "")
        if text:
            PostData.objects.create(text=text)
            return redirect(request.path)

    posts = PostData.objects.all().order_by("-id")
    return render(request, "home.html", {"posts": posts})
