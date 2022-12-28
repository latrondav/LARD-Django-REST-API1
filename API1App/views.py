from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *

# Create your views here.
def drink_list(request):

    #get all the drinks
    drinks = Drink.objects.all()
    #serialize them
    serializer = DrinkSerializer(drinks, many=True)
    #return json
    return JsonResponse(serializer.data, safe=False)