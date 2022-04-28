from rest_framework import serializers

from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User


class RegistartionAccount(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=150, validators=[UniqueValidator(
        User.objects.all(), 'Такой логин уже зарегистрирован')])
    password = serializers.CharField(required=True)
    password_repeat = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password_repeat']:
            raise serializers.ValidationError(
                {'password': 'Пароли не совпадают'})
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('__all__')
