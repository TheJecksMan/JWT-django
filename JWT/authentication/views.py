import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


from rest_framework.decorators import api_view


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
                "ErrorCode": 1,
                'username': user.username,
                'firstname': user.first_name,
                'lastname': user.last_name,
                'date_joined': user.date_joined,
                'sessionid': request.session.session_key
            })
    else:
        return JsonResponse({"ErrorCode": -1, "ErrorDesc": "Что то пошло не так"})


def reset_password(request):
    pass


def edit_profile(request):
    json_data = json_worker(request)


# @api_view('POST')
# def rest_sign_in(request):
#     if request.method == 'POST':
#         pass


def json_worker(request):
    return json.loads(request.body.decode('utf-8'))
