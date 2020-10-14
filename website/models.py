from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import JSONField
from organizer.models import Enterprise, Tag
from core.models import AbstractBaseModel


class Post(AbstractBaseModel):
    title = models.CharField(_("title"),
                             max_length=128,
                             db_index=True,
                             blank=False,
                             )
    slug = models.SlugField(_("slug"),
                            max_length=128,
                            unique=True,
                            )
    content = JSONField(_("content"), blank=False, default=dict)
    pub_date = models.DateTimeField(_("date published"))
    tags = models.ManyToManyField(Tag, blank=True,
                                  verbose_name=_("tags"),
                                  related_name="post",)
    enterprise = models.ForeignKey(
        Enterprise, on_delete=models.CASCADE,
        verbose_name=_("enterprise"),
        related_name="post",)

    def __str__(self):
        return self.title

    class Meta:
        get_latest_by = "pub_date"
        ordering = ["-pub_date"]
        unique_together = ("slug", "title")
        verbose_name = _("website post")
        verbose_name_plural = _("website posts")
