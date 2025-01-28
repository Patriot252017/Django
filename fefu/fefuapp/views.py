from django.shortcuts import render, redirect
from .models import PostData
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json

def post_list_and_create(request):
    if request.method == "POST":
        text = request.POST.get("text", "")
        if text:
            PostData.objects.create(text=text)
            return redirect(request.path)

    posts = PostData.objects.all().order_by("-id")
    return render(request, "home.html", {"posts": posts})

@csrf_exempt
def create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if username and password and email:
            user = User.objects.create_user(username=username, password=password, email=email)
            return JsonResponse({'id': user.id, 'username': user.username}, status=201)
        return JsonResponse({'Missing required fields'}, status=400)

def get_users(request):
    if request.method == 'GET':
        users = User.objects.all().values('id', 'username', 'email')
        return JsonResponse(list(users), safe=False)

def get_user(request, user_id):
    if request.method == 'GET':
        user = get_object_or_404(User, pk=user_id)
        return JsonResponse({'id': user.id, 'username': user.username, 'email': user.email})

@csrf_exempt
def update(request, user_id):
    if request.method == 'PUT':
        user = get_object_or_404(User, pk=user_id)
        data = json.loads(request.body)

        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        if 'password' in data:
            user.set_password(data['password'])

        user.save()
        return JsonResponse({'message': 'User updated successfully'}, safe=False)

@csrf_exempt
def delete(request, user_id):
    if request.method == 'DELETE':
        try:
            user = User.objects.get(pk=user_id)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'}, safe=False)
        except User.DoesNotExist:
            return JsonResponse({'error': f'User with id {user_id} not found'}, status=404, safe=False)