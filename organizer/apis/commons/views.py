from rest_framework.viewsets import ModelViewSet
from organizer.apis.commons.serializers import \
    (
    ReadTagSerializer,
    WriteTagSerializer,
    WriteEnterpriseSerializer,
    ReadEnterpriseSerializer,
    ReadNewsLinkSerializer,
    WriteNewsLinkSerializer,
    )

from organizer.models import Tag, Enterprise, NewsLink


class TagViewSet(ModelViewSet):
    serializer_class = WriteTagSerializer
    read_serializer_class = ReadTagSerializer
    lookup_field = "slug"
    queryset = Tag.objects.all()
    ordering_fields = ("slug",)
    ordering = ("slug",)


class EnterpriseViewSet(ModelViewSet):
    serializer_class = WriteEnterpriseSerializer
    read_serializer_class = ReadEnterpriseSerializer
    lookup_field = "slug"
    queryset = Enterprise.objects.all()
    ordering_fields = ("slug", "-founded_date",)
    ordering = ("-founded_date",)


class NewsLinkViewSet(ModelViewSet):
    serializer_class = WriteNewsLinkSerializer
    read_serializer_class = ReadNewsLinkSerializer
    lookup_field = "slug"
    queryset = NewsLink.objects.all()
    ordering_fields = ("slug", "-pub_date", "enterprise__name",)
    ordering = ("-pub_date",)
