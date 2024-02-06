from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status, request
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from usermanagement.models import User_Management
from usermanagement.serializers import UserManagementProfileRegisterSerializer, UserManagementLoginSerializer, \
    UserProfileSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrAdmin
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework.decorators import action



class RegisterView(generics.CreateAPIView):
    queryset = User_Management.objects.all()
    serializer_class = UserManagementProfileRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        response_data = {
            'message': 'User successfully registered.',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class LoginView(generics.CreateAPIView):
    serializer_class = UserManagementLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        user_instance = serializer.validated_data.get('user')
        print('user data is ', user_instance)
        # if not isinstance(user, CustomeUserProfile):
        #     return Response({'error': 'Invalid user object'}, status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user_instance)
        access_tokens = AccessToken.for_user(user_instance)
        response_data = {
            'refresh': str(refresh),
            'access': str(access_tokens),
        }
        return Response(response_data, status=status.HTTP_200_OK)


class UserInfo():
    logged_in_user = {}


def _login(request):
    from django.http import HttpResponse
    from django.shortcuts import redirect
    if request.method == 'POST':
        # print(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            # request.session.set_expiry(86400) #sets the exp. value of the session
            login(request, user)  # the user is now logged in
        return redirect('/api/v1/docs')
    else:
        from django.shortcuts import render
        return render(request, 'login.html')


def _logout(request):
    from django.shortcuts import redirect
    request.session.flush()
    return redirect('/api/v1/docs')


class UserProfileList(generics.ListCreateAPIView):
    queryset = User_Management.objects.all()
    # serializer_class = CustomUserProfileSerializer
    serializer_class = UserProfileSerializer
    # permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    permission_classes = [permissions.AllowAny]
    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user.username)


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User_Management.objects.all()
    serializer_class = UserProfileSerializer
    # permission_classes = [permissions.AllowAny]
    # permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user.username)

    # @action(detail=True, methods=['put'])
    # def update_profile(self, request, pk=None):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(modified_by=request.user.username)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get_serializer_class(self):
        switcher = {
            'GET': UserProfileSerializer,
            'PUT': UserProfileSerializer,
            'DELETE': UserProfileSerializer,
            'PATCH': UserProfileSerializer
        }
        return switcher[self.request.method]
