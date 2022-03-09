import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def generations_tokens(request):
    pass


@csrf_exempt
def sing_up(request):  # Регистрация

    json_data = json_worker(request)

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
                return JsonResponse({"ErrorCode": 0, "ErrorDesc": "Пользователь создан"})
            else:
                return JsonResponse({"ErrorCode": -1, "ErrorDesc": "Такой пользователь уже существет"})
        else:
            return JsonResponse({"ErrorCode": -1, "ErrorDesc": "Email уже зарегистрирован"})

    else:
        return JsonResponse({"ErrorCode": -1, "ErrorDesc": "Пароли не совпадают"})


@csrf_exempt
def sing_in(request):
    json_data = json_worker(request)

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
        return JsonResponse({"ErrorCode": -1, "ErrorDesc": "Что то пошло не так"})


def json_worker(request):
    return json.loads(request.body.decode('utf-8'))
