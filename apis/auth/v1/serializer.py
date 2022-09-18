from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(),
                                    message='this email already associated with user try sign in')]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = (
            'email',
            'password',
        )
        extra_kwargs = {
            'email': {'required': True}
        }

    def create(self, validated_data):
        with transaction.atomic():
            validated_data['username'] = self.generate_username(validated_data['email'].split('@')[0].replace('+', ''))
            user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                is_active=True
            )

            user.set_password(validated_data['password'])
            user.save()
            return user

    @staticmethod
    def generate_username(user_name):
        ln = User.objects.filter(username__icontains=user_name).count()
        return f'{user_name}@{ln + 1}' if ln > 0 else user_name


class CustomJWTSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        credentials = {
            'username': '',
            'password': attrs.get("password")
        }

        user_obj = User.objects.filter(email=attrs.get("username")).first() or User.objects.filter(
            username=attrs.get("username")).first()
        if user_obj:
            credentials['username'] = user_obj.username

        return super().validate(credentials)
