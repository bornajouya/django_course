from rest_framework import serializers, viewsets
from loginAPI.models import Users, Comment, Token


# Serializers define the API representation.
class SimpleUserSerializer(serializers.ModelSerializer):
    cover = serializers.SerializerMethodField()

    def get_cover(self, instance):
        print(instance)
        print(type(instance))
        return str(instance.user_photo)

    class Meta:
        model = Users
        fields = ['id', 'user_name', 'user_lastname', 'cover']


class CreateUserSerializer(serializers.ModelSerializer):
    cover = serializers.SerializerMethodField()

    def get_cover(self, instance):
        print(instance)
        print(type(instance))
        return str(instance.user_photo)

    def create(self, validated_data):
        return Users.objects.create(**validated_data)

    class Meta:
        model = Users
        fields = ['id', 'user_name', 'user_lastname', 'cover']


class TokenSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Token.objects.create(**validated_data)

    class Meta:
        model = Token
        fields = ['token', 'user']


class CommnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'email', 'datetime', 'book', 'text']

    def to_representation(self, value):
        finall = super().to_representation(value)
        finall["cover"] = ""
        return finall
