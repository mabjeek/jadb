from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
	
def login(request):
	"""login page"""
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user and user.is_active:
				#login(request)
				return HttpResponse('User successfully logged in')
			else:
				return HttpResponse('Incorrect login/password')
	else:
		form = LoginForm()
		
	return render_to_response("login.html", {'login_form': form}, context_instance=RequestContext(request))