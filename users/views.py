from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.views import status
from rest_framework.response import Response
from users.models import User
from rest_framework_jwt.utils import jwt_payload_handler
import jwt
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from rest_framework.generics import RetrieveUpdateAPIView


from users.serializers import UserSerializer
from django.shortcuts import render

class CreateUser(APIView):
    # Allow any user (authenticated or not) to access this url 
    permission_classes = (AllowAny,)
 
    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginUser(APIView):

    permission_classes = (AllowAny,)
 
    def post(self, request):
 
        try:
            email = request.data['email']
            password = request.data['password']
    
            user = User.objects.get(email=email, password=password)
            if user:
                try:
                    payload = jwt_payload_handler(user)
                    token = jwt.encode(payload, settings.SECRET_KEY)
                    user_logged_in.send(sender=user.__class__,
                                        request=request, user=user)

                    response = {
                        'name':"%s %s" % (user.first_name, user.last_name),
                        'token':token,
                        'status':status.HTTP_200_OK
                    }
                    return Response(response)
    
                except Exception as e:
                    raise e
            else:
                response = {
                    'error': 'invalid email or password or the account has been deactivated',
                    'status':status.HTTP_403_FORBIDDEN
                }
                return Response(response)
        except KeyError:
            response = {
                    'error': 'please provide a email and a password',
                    'status':status.HTTP_403_FORBIDDEN
            }
            return Response(response)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
 
    # Allow only authenticated users to access this url
    serializer_class = UserSerializer
 
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
 
    def put(self, request, *args, **kwargs):
 
        serializer = UserSerializer(
            request.user, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
 
        return Response(serializer.data, status=status.HTTP_200_OK)