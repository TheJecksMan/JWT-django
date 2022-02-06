from django.http import HttpResponse

from authlib.jose import jwt
import json

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


private_key = '''-----BEGIN RSA PRIVATE KEY-----
MIIBOQIBAAJAdNrvKFDoAedA9uE855bC4APqH8UGiafeY9arXoX3UKM1tezkEuJH
G6L9pGwZafANJ3hfYiYJQEEKO64E4r+lOQIDAQABAkA88cIxgKC//WAAYlBlaFeS
hfghQZy7RnXSFC+kSLJHt2HyknAmkmkBmhVOgXC/OZMs6a+GEaG3fcpnevqDTJQB
AiEAv/vdhxunLn8+73s2+dWmDgKDHcsGkHS37NQkvAgK0lkCIQCb0e86BqP8Y69p
FQ3xSZ0dcbySCD1Xtj0I33teYLhN4QIhAIzhamKm7Du2rJxYMrOLEFvfhA/s2FhR
DlcAJiTFUguhAiBpzhqIJzwwxCu2yfImtlq2RKXL70ZgCcHWBZJK2pgrYQIgM/c1
t6aZ1ksFPXF92meLf3xaknQ68zFduGBmjewaVk4=
-----END RSA PRIVATE KEY-----'''


public_key = '''-----BEGIN PUBLIC KEY-----
MFswDQYJKoZIhvcNAQEBBQADSgAwRwJAdNrvKFDoAedA9uE855bC4APqH8UGiafe
Y9arXoX3UKM1tezkEuJHG6L9pGwZafANJ3hfYiYJQEEKO64E4r+lOQIDAQAB
-----END PUBLIC KEY-----'''


def encode_token(payload):
    # Подготовка токена
    header = {"alg": "RS256"}
    # payload = {"email": "test1@inbox.ru",
    #            "username": "test1",
    #            "password1": "12345",
    #            "password2": "12345"}
    token = jwt.encode(header, payload, private_key)
    return token.decode("utf-8")


def decode_token(token):
    # Расшифровка токена
    claims = jwt.decode(token, public_key)
    return claims


def get_token(request):
    try:
        token = request.headers['Authorization']  # Получение заголовка
    except:
        return HttpResponse('Отсутсвует заголовок')

    token = token.replace('Bearer', '').strip()
    return decode_token(token)


def generations_tokens(request):
    return HttpResponse(encode_token(json.loads(request.GET['data'])))


def sing_up(request):  # Регистрация
    try:
        json_data = str(get_token(request))
        json_object = json_data.replace("'", '"')
        json_data = json.loads(json_object)  # Преобразование в словарь
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
            return HttpResponse('Email уже зарегистрирован')
    else:
        return HttpResponse('Пароли не совпадают')


def sing_in(request):
    json_data = str(get_token(request))
    json_object = json_data.replace("'", '"')
    json_data = json.loads(json_object)  # Преобразование в словарь

    username = json_data['username']
    password = json['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse('Вход был успешно произведён!')
    else:
        return HttpResponse('Ошибка')
