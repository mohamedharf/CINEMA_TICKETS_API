from django.shortcuts import render
from django.http.response import JsonResponse 
from .models import Guest , Movie , Reservation
from rest_framework.decorators import api_view
from .serializers import GuestSerializer , MovieSerializer , ReservationSerializer
from rest_framework import status , filters
from rest_framework.response import Response
#without rest_framework and no query  (FPV)

def no_rest_no_model(request):
    
    
    guests=[
        
        {
         'id':1,
         'name':'mohamed',
         'phone':'0123456789',
         'email':'mohamed@gmail.com'   
            
        },
        {
         'id':2,
         'name':'ahmed',
         'phone':'0123456789',
         'email':'ahmed@gmail.com'   
            
        },
        {
         'id':3,
         'name':'ali',
         'phone':'0123456789',
         'email':'ali@gmail.com'   
            
        }, 
    ]
    return JsonResponse(guests, safe=False)





# no rest  models data

def no_rest_from_model(request):
    data = Guest.objects.all()
    response={
        
        'guests':list(data.values('name' , 'phone' , 'email'))
    }
    return JsonResponse(response)


#list == Get
# create == Post
# pk query == Get
# update == Put
# delete   DEStroy== Delete


#3 functions beasd views
#3.1 Get post
@api_view(['GET' , 'POST'])
def FBV_list(request):
    #git
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests , many=True)
        return Response(serializer.data)
    #post
    elif request.method == 'POST':
        serializer = GuestSerializer(data = request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status =status.HTTP_201_CREATED)
        return Response(serializer.data , status = status.HTTP_400_BAD_REQUEST)

#git put delete
#@api_view()
#def