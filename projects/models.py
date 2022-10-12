from uuid import UUID
from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    vote_total=models.IntegerField(default=0,null=True,blank=True)
    vote_ratio=models.IntegerField(default=0,null=True,blank=True)
    demo_link=models.CharField(max_length=2000,null=True,blank=True)
    tag=models.ManyToManyField('Tag',blank=True)
    source_link=models.CharField(max_length=2000,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.title
class Reviews(models.Model):
    VOTE_TYPE=(
        ('Up','Up Vote'),
        ('Down','Down Vote'),
    )
    # owner=
    Project=models.ForeignKey(Project, on_delete=models.CASCADE)
    body=models.TextField(null=True,blank=True)
    Value=models.CharField(max_length=200, choices=VOTE_TYPE)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.Value

class Tag(models.Model):
    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.name
