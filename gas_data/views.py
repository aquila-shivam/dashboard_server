# Create your views here.
# gas_data/views.py

from django.http import JsonResponse
from .models import GasData

def get_gas_data(request):
    gas_data = GasData.objects.all().values(
        'intensity', 'likelihood', 'relevance', 'end_year', 'country', 'topic', 'region'
    )
    return JsonResponse(list(gas_data), safe=False)

def say_hello(request):
    return JsonResponse('Hello',safe=False)