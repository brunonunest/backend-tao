from rest_framework import serializers
from organizer.models import Tag


class ReadTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = (
            "name",
            "slug",
        )
        read_only_fields = fields


class WriteTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = (
            "name",
            "slug",
        )
