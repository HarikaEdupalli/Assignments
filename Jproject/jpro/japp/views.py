from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User #bult in User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.http import JsonResponse
from.serializers import UserSerializer,ProSerializer
from .models import Pro
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        User.objects.create_user(username, email, password)
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
           
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Logged in successfully'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
 
def logout_view(request):
    logout(request)
    return JsonResponse({'success': True, 'message': 'Logged out successfully'})
class DeleteView(APIView):
    def delete(self,request,username):
        try:
         user=User.objects.get(username=username)
         user.delete()
         return Response({"message": "User deleted successfully"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
         return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
class GetView(APIView):
    def get(self,request):
        user=User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   
class Get_ProductsView(APIView):
    def get(self,request):
        user=Pro.objects.all()
        serializer = ProSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
 