from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from apps.account.serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, UserChangePasswordSerializer, ForgotPasswordSerializer, NewResetPasswordSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from apps.songs.models import Song
# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token: ': token, 'msg:': 'Registration Successfull'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserLoginView(APIView):

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token: ': token,'msg':'Login Successfull'}, status=status.HTTP_200_OK)
            
            else:
                return Response({'errors':{'non_field_errors' : ['Email or Password is not valid']}}, status=status.HTTP_404_NOT_FOUND) 


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class UserChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(data=request.data, context = {'user':request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Successfully Changed'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ForgotPasswordView(APIView):

    def post(self, request, format = None):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'Password Reset link is sent, please check your email'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class NewResetPasswordView(APIView):
    
    def post(self, request, uid, token, format=None):
        serializer = NewResetPasswordSerializer(data=request.data, context= {'uid':uid, 'token': token})
        if serializer.is_valid(raise_exception=True):
            return Response({"msg":"Password RESET Successfully!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddFavoriteSong(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, song_id, format=None):
        try:
            song = Song.objects.get(pk=song_id)
            user = request.user

            if song not in user.favorite_songs.all():
                user.favorite_songs.add(song)
                return Response({'message': 'Song added to favorites'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Song is already in favorites'}, status=status.HTTP_400_BAD_REQUEST)
        except Song.DoesNotExist:
            return Response({'message': 'Song not found'}, status=status.HTTP_404_NOT_FOUND)
