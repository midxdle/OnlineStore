from rest_framework import serializers
from rest_framework.fields import ReadOnlyField, SerializerMethodField
from .models import *
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User






class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ( 
            'id',
            'first_name',
            'last_name',
            'email',
            'password',    
        )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password':{'write_only':True},
            'profileimage':{'write_only':True},
            'birth_date': {'required': True},
            'phone_number': {'required': True},
            'years_driving_license': {'required': True},
            'negative_drivinglicense_point': {'required': True},
            'years_pco_license': {'required': True},
            'accident_number': {'required': True},
            'address': {'required': True},
        }
        read_only_fields = ('id', 'signed_up_from_app')
    

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],  
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    