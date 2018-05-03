from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from hh.models import Bar, HappyHour
from hh.serializers import BarSerializer, HappyHourSerializer
from rest_framework import generics
from decimal import Decimal


def index(request):
    return render(request, 'frontcontent.html')

def userProfileView(request):
    return render(request, 'userprofile.html')

def all_bars(request):
    context = {
        'bars': Bar.objects.all(),
        'happyhours':HappyHour.objects.all(),
    }
    return render(request, 'barcontent.html', context)

def barView(request, slug):
    bar = get_object_or_404(Bar, slug=slug)
    happyhours = HappyHour.objects.filter(bar=bar.pk)
    return render(request, 'singlebar.html', {'bar':bar, 'happyhours':happyhours})

def about(request):
    return render(request, 'aboutcontent.html')

class BarListCreate(generics.ListAPIView):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer

class HHListCreate(generics.ListAPIView):
    queryset = HappyHour.objects.all()
    serializer_class = HappyHourSerializer

class MapBarListCreate(generics.ListAPIView):
    serializer_class = BarSerializer

    def get_queryset(self):
        """
        This view should return a list of the bars within 2 coordinates (lat lng)
        """
        latN = Decimal(self.kwargs['latN'])
        lngW = Decimal(self.kwargs['lngW'])
        latS = Decimal(self.kwargs['latS'])
        lngE = Decimal(self.kwargs['lngE'])

        # Latitude North is Big, South is small
        # Longitude East is big, West is small
        return Bar.objects.filter(latitude__lt=latN, latitude__gt=latS, longitude__lt=lngE, longitude__gt=lngW)

def map(request):
    return render(request, 'mapdemo.html')

def dataviz(request):
    return render(request, 'dataviz.html')
