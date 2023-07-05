from django.contrib.auth import get_user_model
from rest_framework import renderers, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.account import (
    AuthTokenSerializer,
    UserLoginSerializer)

User = get_user_model()


class UserObtainTokenAPIView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = (renderers.JSONRenderer, renderers.AdminRenderer)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserLoginSerializer(instance=user)
        details = user_serializer.data
        details.update(token=token.key)
        return Response(details)


user_login_api_view = UserObtainTokenAPIView.as_view()


class LogoutAPIView(APIView):
    serializer_class = None
    
    def get(self, request):
        request.user.auth_token.delete()

        return Response(
            status=status.HTTP_200_OK,
            data={"message": "You have successfully logged out"},
        )


user_logout_view = LogoutAPIView.as_view()
