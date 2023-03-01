from django import forms
from .models import Parameter

class ParameterForm(forms.ModelForm):
	class meta:
		model = Parameter
		fields = ("params")