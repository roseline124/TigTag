from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from .models import Customer, WaitingList
from .serializers import CustomerSerializer, WaitingListSerializer
from rest_framework import viewsets
import urllib.request as urllib2
import json 

class CustomerViewSet(viewsets.ModelViewSet) :

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_queryset(self) :
        queryset = Customer.objects.all()

        waiting_number = self.request.query_params.get('waiting_number', None)

        if waiting_number is not None : 
            queryset = Customer.objects.filter(waiting_number=waiting_number)

        return queryset


class WaitingListViewSet(viewsets.ModelViewSet) :

    queryset = WaitingList.objects.all()
    serializer_class = WaitingListSerializer

    def get_queryset(self) :
        queryset = WaitingList.objects.all()
        customer_id = self.request.query_params.get('customer_id', None)

        if customer_id is not None : 
            queryset = WaitingList.objects.filter(customer_id=customer_id)

        return queryset

def request_index(request) :
    data = Customer.objects.filter(tag_time__lte=timezone.now()).order_by('tag_time')    

    return render(request, "tigtag/index.html", {'data':data}) 


def request_waiting_list(request) :
    data = Customer.objects.filter(tag_time__lte=timezone.now()).order_by('tag_time')    

    return render(request, "tigtag/waiting_list.html", {'data':data}) 