from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class RoleChoice(models.TextChoices):
    PLANNER = "planner", _("planner")
    SALES_MANAGER = "sales_manager", _("sales_manager")


class ProcessChoice(models.TextChoices):
    CHANGEMATERIAL = "CHANGEMATERIAL", _("CHANGEMATERIAL")
    CREATEMATERIAL = "CREATEMATERIAL", _("CREATEMATERIAL")

