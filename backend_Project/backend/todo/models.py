from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    tag = models.ManyToManyField("Tag", related_name="tags", blank=True)

    def _str_(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length=30)

    def _str_(self):
        return self.name