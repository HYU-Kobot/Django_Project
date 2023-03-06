import json
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from django.views.decorators.csrf import csrf_exempt
from .models import Parameter
from .forms import ParameterForm
from .serializers import ParameterSerializer
from django.utils.decorators import method_decorator
from django.http import HttpResponse

def index(request):
	message = request.GET.get('period_buy')
	print(message)

	return HttpResponse("backtest")

class ParameterList(APIView):
	def get(self, request):
		parameters = Parameter.objects.all()

		serializer = ParameterSerializer(parameters, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = ParameterSerializer(
			data = request.data
		)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @method_decorator(csrf_exempt, name="dispatch")
# def parameter_value(request):
# 	if request.method == "GET":
# 		form = ParameterForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return HttpResponse(json.dumps({"status": "Success"}))
# 		else:
# 			return HttpResponse(json.dumps({"status": "Failed"}))

class ParameterView(viewsets.ModelViewSet):
    serializer_class = ParameterSerializer
    queryset = Parameter.objects.all()


# @method_decorator(csrf_exempt, name="dispatch")
# def backtest(request):
# 	if request.method == "GET":
# 		return HttpResponse(json.dumps({"status": "Success"}))
# 	elif request.method == "POST":
# 		return HttpResponse(json.dumps({"status": "Failed"}))