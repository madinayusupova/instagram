from django.contrib.auth.decorators import login_required
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from .models import UserFollowing
from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserFollowingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = UserSerializer
    queryset = UserFollowing.objects.all()

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import UserFollowing
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
@login_required()
def user_follow(request):
    print("FUNCTION IS CALLING")
    user_id = request.data.get('id')
    action = request.data.get('action')
    print(request.user)
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            print("USER", user)
            if action == 'follow':
                print("FOLLOWING")
                UserFollowing.objects.get_or_create(kogo_follow=request.user, kto=user)
            else:
                print("UNFOLLOWING")
                UserFollowing.objects.filter(kogo_follow=request.user, kto=user).delete()
                return Response({'status':'unfollowed'})
        except User.DoesNotExist:
            return Response({'status':'user does not exist'})
        return Response({'status':'followed'})
    return Response({'status':'oblom'})




