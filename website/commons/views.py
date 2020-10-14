from rest_framework.viewsets import ModelViewSet
from website.commons.serializers import WritePostSerializer, ReadPostSerializer
from website.models import Post


class PostViewSet(ModelViewSet):
    serializer_class = WritePostSerializer
    read_serializer_class = ReadPostSerializer
    lookup_field = "slug"
    queryset = Post.objects.all()
    ordering_fields = ("title", "pub_date", "date_created", "date_updated", "tags", "enterprise",)
    ordering = ("-date_created",)
