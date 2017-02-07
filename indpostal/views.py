from rest_framework import serializers
#from . import serializers
from django.shortcuts import render
from .models import Pos
from rest_framework import viewsets
from indpostal.Serializers import PosSerializer
from rest_framework import generics


# Create your views here.
def import_db(request):
   
   f = open('/home/bhanu/Desktop/projects/drf/postal/indpostal/csv/all_india_pin_code.csv', 'r')  
   for line in f:
       line =  line.split(',')
       tmp = Pos.objects.create()
       tmp.officename = line[0]
       tmp.pincode= line[1]
       tmp.officeType = line[2]
       tmp.Deliverystatus = line[3]
       tmp.divisionname = line[4]
       tmp.regionname = line[5]
       tmp.circlename = line[6]
       tmp.taluk = line[7]
       tmp.Districtname = line[8]
       tmp.statename = line[9]
       tmp.save()

   f.close()



class PosViewSet(generics.ListCreateAPIView):
        queryset = Pos.objects.all()
        serializer_class = PosSerializer

class PoseingViewset(generics.ListAPIView):
       serializer_class = PosSerializer
       def get_queryset(self):
          x = self.kwargs['x']
          return Pos.objects.filter(pincode=x)

