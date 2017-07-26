from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


@login_required
def index(request):

    context = RequestContext(request)
    context_dict = {'boldmessage': "ABHITAKER"}

    return render_to_response('weblog/home.html', context_dict, context)

@login_required
def diary(request):
    return HttpResponse("FIRST VIEW OF DIARY APPLICATION <a href='/weblog/'> home </a>")

@login_required
def about(request) :

    context = RequestContext(request)
    context_dict = {'user': "ABHITAKER"}

    return render_to_response('weblog/about.html', context_dict, context)

@login_required
def write(request) :
    
    return render_to_response('weblog/write.html')

@login_required
def read(request) :
    
    return render_to_response('weblog/read.html')


