from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, status

from accounts.models import Account

from accounts.apis.auth.serializers import WriteLoginSerializer



"""class LoginViewSet(GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = WriteLoginSerializer
    lookup_field = "username"

@api_view(['GET', 'POST'])
def login_view(request):
    if request.method == 'POST':
        objects = Account.objects.all()
        serializer = WriteLoginSerializer(objects, many=True)
        return Response(serializer.data)"""
