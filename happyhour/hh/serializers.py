from rest_framework import serializers
from hh.models import Bar, HappyHour

class HappyHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = HappyHour
        fields = ['name']

class BarSerializer(serializers.ModelSerializer):
    children = HappyHourSerializer(source='happyhours', read_only=True, many=True)
    #children = serializers.SerializerMethodField('get_alternate_name')

    class Meta:
        model = Bar
        #fields = '__all__'
        fields = ['name', 'children', 'city', 'latitude', 'longitude']
