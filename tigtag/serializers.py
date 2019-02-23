from rest_framework import serializers
from .models import Customer, WaitingList

class CustomerSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Customer
        fields = ( 'waiting_number',
                   'phone_number',
                   'tag_time', )

class WaitingListSerializer(serializers.ModelSerializer) :
    class Meta:
        model = WaitingList
        fields = ( 'customer_id', #waiting_number
                   'waiting_people', )
