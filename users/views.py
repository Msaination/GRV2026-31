from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, ChangePasswordSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


#logout
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()  # requires simplejwt blacklist app enabled
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)




#Change password view to allow users to change their password
class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer 
    # permission_classes = [IsAuthenticated, IsRegistered] # Only registered users can change their password

    def update(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return Response(status=status.HTTP_200_OK)

        if not user.check_password(serializer.validated_data['old_password']): 
            return Response({"old_password": "Wrong password"}, status=status.HTTP_400_BAD_REQUEST) 
        user.set_password(serializer.validated_data['new_password']) 
        user.save() 
        return Response({"detail": "Password updated successfully"}, status=status.HTTP_200_OK)