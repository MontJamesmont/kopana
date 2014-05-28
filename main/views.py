from django.http import HttpResponse
from django.template import loader, RequestContext
from main.models import *
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.sessions.models import Session
from main.forms import *

def signUp(request):
    if request.method == 'POST': # If the form has been submitted
        form = UserFormSignUp(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = UserFormSignUp() # An unbound form
    
    return render(request, 'signUp.html', {
        'form': form,
    })

def signIn(request):
    if request.method == 'POST': # If the form has been submitted...
        form = forms.UserFormSignIn(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            try:
                us = User.objects.get(login=form.data['login'],password=form.data['password'])
                request.session['user'] = us.id
                request.session['login'] = us.login
                request.session['type'] = us.type
            except:
                return HttpResponseRedirect('/signIn/') # Redirect after POST
    else:
        form = UserFormSignIn() # An unbound form

    return render(request, 'signIn.html', {
        'form': form,
    })

def home(request):
    template = loader.get_template('home.html')
    now = datetime.now().date()
    latest_matches = Match.objects.all()
    context = RequestContext(request, {
        'latest_matches': latest_matches,
    })
    return HttpResponse(template.render(context))

def team(request, team_id):
    template = loader.get_template('team.html')
    team = Team.objects.get(id=int(team_id))
    context = RequestContext(request, {'team' : team, })
    return HttpResponse(template.render(context))
