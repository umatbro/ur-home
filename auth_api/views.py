from auth_api.serializers import UserSerializer

from django.contrib import auth
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class LoginView(APIView):
    def post(self, request: Request):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return Response({'msg': 'success'})
        return Response({'msg': 'fail'})


class LogoutView(APIView):
    def post(self, request: Request):
        user = request.user
        auth.logout(request)
        return Response({'msg': f'logged out {user if user else "noone"}'})


class UserDetailsView(APIView):
    def get(self, request: Request):
        if request.user and request.user.is_authenticated:
            return Response(UserSerializer(request.user).data)
        return Response({'msg': 'You are not logged in!'})
