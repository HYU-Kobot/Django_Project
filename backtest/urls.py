from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ParameterList

from . import views

urlpatterns = [
	path('parameter/', ParameterList.as_view()),
]