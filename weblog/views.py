from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import SignUpForm, PostForm
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from .models import Post


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


class PostView(generic.ListView):

    model = Post
    template_name="weblog/home.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PostView, self).dispatch(*args, **kwargs)

