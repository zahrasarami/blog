from rest_framework import serializers
from django.contrib.auth.models import User
from  rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if User.objects.filter(username = data['username']).exists() :
            raise serializers.ValidationError('username is taken')

        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'].lower(),
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        return validated_data



class LoginSerializer(serializers.Serializer) :
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if not User.objects.filter(username = data['username']).exists() :
            raise serializers.ValidationError('account not found')

        return data

    def get_jwt_token(self , data) :
        print(data['username'] , data['password'])
        user = authenticate(username= data['username'] , password=data['password'])
        if not user :
            return {'massege' : 'invalid credentials' , 'data' :{}}

        refresh = RefreshToken.for_user(user)
        return {'massege' : 'seccessful login' , 'data' :{'token' : {'refresh': str(refresh),
        'access': str(refresh.access_token),}}}
    