import uuid

from django.db import models

from model_utils.models import TimeStampedModel


class Club(TimeStampedModel):
    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4,
                            editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name