from django.db import models
from datetime import datetime
# Create your models here.
class createticket(models.Model):
    subject = models.CharField(max_length=200)
    description = models.TextField()
    createdat = models.DateTimeField(default= datetime.now, blank=True)
    createdby = models.TextField()
    priority = models.IntegerField()
    assignedto = models.TextField()
    userId = models.IntegerField()
    ticketId = models.IntegerField()
    def __str__(self):
        return self.subject
    class Meta:
        verbose_name_plural = "Create Ticket"