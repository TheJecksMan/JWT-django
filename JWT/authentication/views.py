import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


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
                return JsonResponse({"ErrorCode": 0, "Desc": "Пользователь создан"})
            else:
                return JsonResponse({"ErrorCode": -1, "Desc": "Такой пользователь уже существет"})
        else:
            return JsonResponse({"ErrorCode": -1, "Desc": "Email уже зарегистрирован"})

    else:
        return JsonResponse({"ErrorCode": -1, "Desc": "Пароли не совпадают"})


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
                "ErrorCode": 0,
                'username': user.username,
                'firstname': user.first_name,
                'lastname': user.last_name,
                'date_joined': user.date_joined.strftime("%d.%m.%Y %H:%M"),
                'sessionid': request.session.session_key
            })
    else:
        return JsonResponse(
            {
                "ErrorCode": -1,
                "Desc": "Некорректный логин или пароль"
            })


@csrf_exempt
def reset_password(request):
    json_data = json_worker(request)

    username = json_data["username"]
    old_password = json_data["old_password"]
    new_password = json_data["new_password"]
    repeat_new_password = json_data["repeat_new_password"]
    if new_password != repeat_new_password:
        return JsonResponse({"Error": -1, "Desc": "Пароли не совпадают"})
    else:
        return JsonResponse({"ErrorCode": 0})


@csrf_exempt
def edit_profile(request):  # редактирование пользовательских данных

    if (request.user.is_authenticated):
        json_data = json_worker(request)

        username = json_data["username"]
        firstname = json_data["firstname"]
        lastname = json_data["lastname"]
        return JsonResponse({"ErrorCode": 0})
    else:
        return JsonResponse({"ErrorCode": -1, "Desc": "Bad Request. User dont auth!"})


@csrf_exempt
def logout_user(request):
    logout(request)  # Выход из аккаунта
    return JsonResponse({"ErrorCode": 0, "Desc": "Logout"})


def json_worker(request):  # десерелизация json
    return json.loads(request.body.decode('utf-8'))


@csrf_exempt
def gener(request):
    text = request.GET['data']
    return HttpResponse("text")
