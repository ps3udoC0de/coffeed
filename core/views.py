from django.shortcuts import render
from django.views.generic import TemplateView
#from django.http import HttpResponse

# Create your views here.

#def TestView(request, **kwargs):
#	return HttpResponse("Hello World")

class SplashView(TemplateView):
	template_name = "index.html"
		
