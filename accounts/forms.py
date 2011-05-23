from django import forms

class LoginForm(forms.Form):
	"""LoginForm"""
	username = forms.CharField(max_length=30)
	password = forms.CharField(max_length=30)	