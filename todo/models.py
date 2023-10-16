from django.db import models
from django.utils import timezone


# Create your models here.
class Todo(models.Model):
    todo_title = models.CharField("Title", max_length=256, blank=False)
    todo_memo = models.TextField("Descriptions", blank=True)
    todo_visible = models.BooleanField("Visible", default=True)
    published_date = models.DateTimeField(
        "Created time", default=timezone.now, editable=False
    )

    def __str__(self):
        return self.todo_title
