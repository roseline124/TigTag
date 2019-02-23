from django.db import models
from django.utils import timezone 

class Customer(models.Model) :

    phone_number = models.CharField(max_length=11)
    tag_time = models.DateTimeField(blank=True, null=True)
    waiting_number = models.AutoField(primary_key=True)
    
    def response(self):
        self.tag_time = timezone.now()
        self.save()

    def __str__(self) :
        return str(self.phone_number)[-4:]

class WaitingList(models.Model) :
    customer_id = models.IntegerField(default=0)
    waiting_people = models.IntegerField(default=0)