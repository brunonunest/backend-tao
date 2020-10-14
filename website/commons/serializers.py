from rest_framework import serializers
from website.models import Post


class ReadPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            "title",
            "slug",
            "content",
            "pub_date",
            "tags",
            "enterprise",
            "date_created",
            "date_updated",
        )
        read_only_fields = fields


class WritePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            "title",
            "slug",
            "content",
            "pub_date",
            "tags",
            "enterprise",
            "date_created",
            "date_updated",
        )
