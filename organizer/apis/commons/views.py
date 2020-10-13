from rest_framework.viewsets import ModelViewSet
from organizer.apis.commons.serializers import ReadTagSerializer, WriteTagSerializer
from organizer.models import Tag


class TagViewSet(ModelViewSet):
    serializer_class = WriteTagSerializer
    read_serializer_class = ReadTagSerializer
    lookup_field = "slug"
    queryset = Tag.objects.all()
    ordering_fields = ("slug",)
    ordering = ("slug",)
