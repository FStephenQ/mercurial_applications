# Create your views here.
from django.http import HttpResponse
from django.template import Template
from django.shortcuts import render_to_response
from mercurial_applications.blog import models

def front(request):
        posts = models.Post.objects.all()
        return render_to_response('blog/front.html',{'posts':posts,})
