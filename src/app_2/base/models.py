from django.db import models
from django.contrib.auth.models import User


class Messages(models.Model):
    class Meta:
        db_table = "messages"

    title = models.CharField(max_length=128)
    content = models.CharField(max_length=256)
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="receiver")
