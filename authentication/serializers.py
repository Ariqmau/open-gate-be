from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model. Handles creation and validation.
    """
    # Ensure email is required and unique
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    # Ensure username is unique
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    # Make the password write-only so it's not returned in API responses
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        """
        Overrides the default create method to handle password hashing.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

    class Meta:
        model = User
        # Fields to include in the serializer
        fields = ('id', 'username', 'email', 'password')