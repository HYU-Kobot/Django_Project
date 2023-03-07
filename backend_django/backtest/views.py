import json
from django.shortcuts import render
from rest_framework import viewsets

from django.views.decorators.csrf import csrf_exempt
from .models import Parameter
from .forms import ParameterForm
from .serializers import ParameterSerializer
from django.utils.decorators import method_decorator
from django.http import HttpResponse

def index(request):
	message = request.GET.get('abc')
	print(message)

	return HttpResponse("backtest")

@method_decorator(csrf_exempt, name="dispatch")
def parameter_value(request):
	if request.method == "GET":
		form = ParameterForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse(json.dumps({"status": "Success"}))
		else:
			return HttpResponse(json.dumps({"status": "Failed"}))

class ParameterView(viewsets.ModelViewSet):
    serializer_class = ParameterSerializer
    queryset = Parameter.objects.all()


# Create your views here.
