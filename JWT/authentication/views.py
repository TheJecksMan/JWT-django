
from django.http import HttpResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authlib.jose import jwt


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


def encode_token():
    # Подготовка токена
    header = {'alg': 'RS256'}
    payload = {'test1': 'test1'}
    token = jwt.encode(header, payload, private_key)
    return token.decode("utf-8")


def decode_token(token):
    # Расшифровка токена
    claims = jwt.decode(token, public_key)
    return claims


class RegistrationAPI(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)


class TestAPI(APIView):
    pass


def test_token(request):
    try:
        token = request.headers['Authorization']  # Получение заголовка
    except:
        return HttpResponse('Отсутсвует заголовок')

    token = token.replace('Bearer', '').strip()
    return HttpResponse(decode_token(token))
