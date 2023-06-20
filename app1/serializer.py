from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from . models import *
class LoginSerializer(serializers.Serializer):
    
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        
        attrs['user'] = user
        return attrs
    


class SignUpSerializer(serializers.ModelSerializer):


    class Meta:

        model = User
        fields = ("username","first_name","last_name","email","password")


    def create(self,valited_data):


        user = User.objects.create(**valited_data)
        user.set_password(valited_data['password'])
        user.save()
        
        profile = Profile.objects.create(
            user=user,
            name=valited_data['first_name'],
            surname=valited_data['last_name']
        )

        return user


class Postserilizer(serializers.ModelSerializer):



    class Meta:

        model = Posts

        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):


    class Meta:

        model = Posts
        fields = ("title","description","image","longitude","latitude")




class ProfileEditSerializer(serializers.ModelSerializer):


    class Meta:
        model = Profile
        fields = ("name","surname","photo")


    


