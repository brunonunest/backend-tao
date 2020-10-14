from rest_framework import serializers
from organizer.models import Tag, Enterprise, NewsLink


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


class WriteEnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = (
            "name",
            "slug",
            "description",
            "founded_date",
            "contact",
            "website",
            "tags",
        )


class ReadEnterpriseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enterprise
        fields = (
            "name",
            "slug",
            "description",
            "founded_date",
            "contact",
            "website",
            "tags",
        )
        read_only_fields = fields


class WriteNewsLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLink
        fields = (
            "name",
            "slug",
            "pub_date",
            "link",
            "enterprise",
        )


class ReadNewsLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsLink
        fields = (
            "name",
            "slug",
            "pub_date",
            "link",
            "enterprise",
        )
        read_only_fields = fields
