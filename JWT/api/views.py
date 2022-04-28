from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from rest_framework.response import Response
from rest_framework import status

from . import serializers


from PIL import Image

import pytesseract

from rest_framework.decorators import parser_classes
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication])
def login_account(request):
    """
    Получение данных, при входе в аккаунт
    """
    user = request.user
    return Response({
        'username': user.username,
        'firstname': user.first_name,
        'lastname': user.last_name,
        'date_joined': user.date_joined.strftime("%d.%m.%Y %H:%M"),
    })


@ api_view(['POST'])
def regustration_account(request):
    """
    Регистрация нового пользователя
    """
    serializer = serializers.RegistartionAccount(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        if user:
            return Response(status=status.HTTP_200_OK)

    return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@parser_classes([FileUploadParser])
def file_orc(request):
    text = pytesseract.pytesseract.image_to_string()
    return Response('test')


class FileUploadView(APIView):
    parser_classes = [FileUploadParser]

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=204)
