from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Position(models.Model):
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        )
    name = models.CharField(max_length=255)


    class Meta:
        ordering = ("my_order",)
        verbose_name_plural = "Positions"

    def __str__(self):
        return str(self.pk)

class Employee(MPTTModel):
    full_name = models.CharField(max_length=255)
    position = models.ForeignKey("Position", related_name="employee", on_delete=models.CASCADE)
    employment = models.DateTimeField()
    salary = models.FloatField()
    parent = TreeForeignKey(
        "self",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="children",
        db_index=True,
    )

    class MPTTMeta:
        order_insertion_by = ["employment"]

    class Meta:
        verbose_name_plural = "Employess"

    def __str__(self):
        return self.full_name
