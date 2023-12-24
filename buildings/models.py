from django.db import models
from django.utils.translation import gettext_lazy as _


class House(models.Model):
    class RoofType(models.TextChoices):
        float = "FR", _("float")
        broken = "BR", _("broken")

    name = models.CharField(
        _("name"),
        max_length=100,
    )

    floor = models.CharField(_("floor"), max_length=100)

    window = models.IntegerField(_("window"), default=0)

    door = models.IntegerField(_("door"), default=0)

    roof = models.CharField(_("type"), choices=RoofType.choices, max_length=100)

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        verbose_name = "House"
        verbose_name_plural = "Houses"
