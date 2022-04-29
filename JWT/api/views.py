from django import views
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from rest_framework.response import Response
from rest_framework import status

from . import serializers


from rest_framework import generics
import cv2 as cv
import pytesseract
import numpy as np
from django.views.decorators.csrf import csrf_exempt


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


@csrf_exempt
def file_orc(request):

    if request.method == 'POST' or request.method == 'FILES':
        f = request.FILES['img']
        receipt_image = f.read()
        nparr = np.frombuffer(receipt_image, np.uint8)
        img_np = cv.imdecode(nparr, 1)

        pytesseract.pytesseract.tesseract_cmd = 'D:\Files\\tesseract\\tesseract.exe'
        text = pytesseract.pytesseract.image_to_string(img_np, lang="rus")
        if not text or len(text.strip()) == 0:
            return render(request, 'api/file_upload.html', {'text': 'Не удалось распознать текст'})
        return render(request, 'api/file_upload.html', {'text': text})
    return render(request, 'api/file_upload.html')
