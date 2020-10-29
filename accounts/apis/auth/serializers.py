from rest_framework import serializers

from accounts.models import Account


class WriteLoginSerializer(serializers.Serializer):

    class Meta:
        model = Account
        fields = ("email", "password", "username",)
