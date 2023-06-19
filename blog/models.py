from django.db import models
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Blog(models.Model):
    STATUS_CHOICES = [("published","PUBLISHED"),("draft","DRAFT")]
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True,related_name="blogs")
    status = models.CharField(choices=STATUS_CHOICES,max_length=50,null=True)

    def __str__(self):
        return self.title



