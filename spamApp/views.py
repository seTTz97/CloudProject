from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.template import loader
from django.http import HttpResponse
from .forms import Spammodel
from .models import Spam
from django.shortcuts import render

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def spam(request):
    template = loader.get_template('spam.html')
    context = {}
    return HttpResponse(template.render(context, request))

def spam_create(request):

    form = Spammodel(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, "home.html")
    context = {
        'form': form
    }
    return render(request,"spam_create.html", context )
