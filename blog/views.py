# Create your views here.
from django.http import HttpResponse
from django.template import Template
from django.shortcuts import render_to_response
from mercurial_applications.blog import models

def front(request):
        posts = models.Post.objects.all()
        return render_to_response('blog/front.html',{'posts':posts,})

def tag(request,tagname=""):
    taglist = models.Tag.objects.filter(name__exact=tagname)
    if taglist.count() == 0:
        return render_to_response('blog/tags.html',{'error':"That's an invalid tag!",'posts':models.Post.objects.all(),})
    tag = taglist[0]
    posts = [post for post in models.Post.objects.all() if tag in list(post.tags.all())]
    if posts.count == 0:
        return render_to_response('blog/tags.hrml',{'tag':tag,'error':"There aren't any posts for that teg yet!",})
    else:
        return render_to_response('blog/tags.html',{'tag':tag,'posts':posts,})
