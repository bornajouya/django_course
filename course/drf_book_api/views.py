from django.shortcuts import render
from rest_framework import viewsets
from loginAPI.models import Users, Comment
from .serializer import SimpleUserSerializer, CommnetSerializer
from rest_framework import pagination
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.views import View
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import MyUser
from django.http import JsonResponse
from rest_framework.decorators import  permission_classes
from rest_framework import permissions


# @api_view(["GET", "POST"])
@permission_classes((permissions.AllowAny,))
class LoginView(APIView):

    def get(self, request):
        user_name = request.GET.get("user_name")
        phone = request.GET.get("phone")

        if User.objects.filter(username=str(user_name)).exists():
            user = User.objects.get(username=str(user_name))
        else:
            user = MyUser(username=str(user_name),phone_number=str(phone))
            user.save()
        token = Token.objects.get_or_create(user=user)

        return JsonResponse({"Token": str(token)}, status=200, safe=False)


# ViewSets define the view behavior.

class CustomPagination(pagination.PageNumberPagination):
    page_size = 6
    max_page_size = 1000


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Users.objects.all()
    serializer_class = SimpleUserSerializer


class SaveUesrViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = SimpleUserSerializer


class CommnetViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    pagination_class = CustomPagination
    serializer_class = CommnetSerializer
