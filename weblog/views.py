from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, PostForm
from django.views.decorators.csrf import csrf_exempt



@login_required
def index(request):

    context = RequestContext(request)
    user = request.user
    context_dict = {
    "user" : user,
    }

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
@csrf_exempt
def write(request) :
    context = RequestContext(request)
    user = request.user

    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()

    context_dict = {
    "user" : user,
    "form" : form,
    }
    return render_to_response('weblog/write.html',context_dict, context)

@login_required
def read(request) :
    
    return render_to_response('weblog/read.html')


