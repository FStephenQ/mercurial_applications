from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return render_to_response("core_page/index.html")

def bio(request):
	return render_to_response("core_page/bio.html")
