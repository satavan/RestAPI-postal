from rest_framework import serializers
from indpostal.models import Pos


class PosSerializer(serializers.ModelSerializer):
   #owner = serializers.ReadOnlyField(source='owner.username')
   class Meta:
       model=Pos
       fields =('officename','pincode','officeType','Deliverystatus','divisionname','regionname','circlename','taluk','Districtname','statename')

