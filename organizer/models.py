from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import AbstractBaseModel


class Tag(AbstractBaseModel):
    name = models.CharField(_("name"),
                            max_length=128,
                            unique=True,
                            blank=False,
                            null=False
                            )
    slug = models.SlugField(_("slug"),
                            max_length=128,
                            unique=True,
                            help_text="A label for url config",

                            )
    """ Ordenação padrão, outros orderings/filters... nos viewsets """

    class Meta:
        verbose_name = _("Tag")
        ordering = ["name"]
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.name


class Enterprise(AbstractBaseModel):
    name = models.CharField(_("name"),
                            max_length=128,
                            db_index=True)
    slug = models.SlugField(_("slug"),
                            max_length=128,
                            unique=True,
                            help_text="A label for url config",
                            db_index=True
                            )
    description = models.TextField(_("description"), blank=False)
    founded_date = models.DateTimeField(_("date founded"))
    contact = models.EmailField(_("email address"), unique=True)
    website = models.URLField(_("website"), max_length=255)
    tags = models.ManyToManyField(Tag, blank=True,
        verbose_name=_("tags"),
        related_name="enterprise",)

    class Meta:
        get_latest_by = "founded_date"
        ordering = ["name"]
        verbose_name = _("Enterprise")

    def __str__(self):
        return self.name


class NewsLink(AbstractBaseModel):
    name = models.CharField(_("name"),
                            max_length=128,
                            unique=True,
                            blank=False,
                            null=False
                            )
    slug = models.SlugField(_("slug"),
                            max_length=128,
                            unique=True,
                            )
    pub_date = models.DateTimeField(_("date published"))
    link = models.URLField(_("link"), max_length=255)
    enterprise = models.ForeignKey(
        Enterprise, on_delete=models.CASCADE,
        verbose_name=_("Enterprise"),
        related_name="newslink",
    )

    class Meta:
        get_latest_by = "pub_date"
        ordering = ["-pub_date"]
        unique_together = ("slug", "enterprise")
        verbose_name = _("news article")

    def __str__(self):
        return self.name
