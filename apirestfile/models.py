from django.db import models
from model_utils.models import TimeStampedModel


class Fileupload(TimeStampedModel):
    xid = models.CharField( max_length=50, unique=False)    
    ts = models.CharField(max_length=50, unique=False)
    dado = models.CharField(max_length=50, unique=False) 

    def __str__(self):
        return self.xid
