from django import forms
from app0.models import Books_model

class Bookform(forms.ModelForm):
	class Meta:
		model = Books_model
		fields = "__all__"