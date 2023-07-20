from django.contrib.auth import authenticate
from rest_framework import status
from .models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .serializers import AuthenticationSerializer

@api_view(['POST'])
def authorization_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        try:
            token = Token.objects.get(user=user)
        except Token.DoesNotExist:
            token = Token.objects.create(user=user)
        return Response(data={'token': token.key})
    return Response(data={'error': 'ошибка'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def confirm_user(request):
    if request.method == 'POST':
        confirmation_code = request.data.get('confirmation_code')

        try:
            user = get_object_or_404(CustomUser, confirmation_code=confirmation_code, is_active=False)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Invalid confirmation code'}, status=400)

        user.is_active = True
        user.save()

        return Response({'message': 'User confirmed successfully'}, status=200)


@api_view(['POST'])
def register_view(request):
    serializer = AuthenticationSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        return Response(data={'message': 'Successfully registered', 'user': user.username}, status=status.HTTP_201_CREATED)
    return Response(data={'error': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
