from django.http import HttpResponse, JsonResponse

from .api.json_jwt import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def generations_tokens(request):
    return HttpResponse(encode_token(request.GET['data']))


def sing_up(request):  # Регистрация
    try:
        json_data = get_token(request)
    except:
        return HttpResponse('Token not valid')

    email = json_data['email']
    username = json_data['username']
    password1 = json_data['password1']
    password2 = json_data['password2']
    if password1 == password2:  # Проверка валидности пароля
        # Проверка валидности email
        if not User.objects.filter(email=email).exists():
            # Проверка валидности имени
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(
                    username, email, password1)

                user.save()  # Создание пользователя
                return HttpResponse('Пользователь создан')
            else:
                return HttpResponse('Такой пользователь уже существет')
        else:
            return HttpResponse('Email уже зарегистрирован', status=404)
    else:
        return HttpResponse('Пароли не совпадают')


def sing_in(request):
    try:
        json_data = get_token(request)
    except:
        return HttpResponse('Token not valid')

    username = json_data['username']
    password = json_data['password_user']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse(
            {
                'username': user.username,
                'sessionid': request.session.session_key
            })
    else:
        return HttpResponse('Ошибка')
