from socket import RCVALL_SOCKETLEVELONLY
from django.http import HttpResponse

from authlib.jose import jwt
import json


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


# Создание токена
def encode_token(payload):
    # Сравнение типов
    if isinstance(payload, str):
        payload = json.loads(payload)

    header = {"alg": "RS256"}
    # payload = {"email": "test1@inbox.ru","username": "test1","password1": "12345","password2": "12345"}
    token = jwt.encode(header, payload, private_key)
    return token.decode("utf-8")


# Расшифровка токена
def decode_token(token):
    claims = jwt.decode(token, public_key)
    return str(claims)

# Получение токена и его десериализация


def get_token(request):
    try:
        # Получение заголовка
        token = request.headers['Authorization']
    except:
        return HttpResponse('Отсутсвует заголовок')

    token = token.replace('Bearer', '').strip()
    token = decode_token(token)

    json_object = token.replace("'", '"')
    json_data = json.loads(json_object)
    print(token)

    return json_data
