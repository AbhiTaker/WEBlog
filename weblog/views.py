from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):

    context = RequestContext(request)
    context_dict = {'boldmessage': "ABHITAKER"}

    return render_to_response('weblog/index.html', context_dict, context)

def diary(request):
    return HttpResponse("FIRST VIEW OF DIARY APPLICATION <a href='/weblog/'> home </a>")

