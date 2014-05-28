from django.http import HttpResponse
from django.template import loader, RequestContext
from main.models import Match, Team, Season, Matchday, Round
from main.forms import SeasonForm
from datetime import datetime
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect

def signUp(request):
    if request.session.user != Null:
        return HttpResponseRedirect('/team/')
    else:
        if request.method == 'POST': # If the form has been submitted
            form = UserForm(request.POST) # A form bound to the POST data
            if form.is_valid(): # All validation rules pass
                form.save()
                return HttpResponseRedirect('/') # Redirect after POST
        else:
            form = UserForm() # An unbound form
    
        return render(request, 'sign_up.html', {
            'form': form,
        })

def signIn(request):
    if request.method == 'POST': # If the form has been submitted...
        form = UserForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            try:
                us = User.objects.get(login=form.data['login'],password=form.data['password'])
                request.session['user'] = us.id
                request.session['login'] = us.login
                request.session['type'] = us.type
            except:
                return HttpResponseRedirect('/sign_in/') # Redirect after POST
    else:
        form = UserForm() # An unbound form

    return render(request, 'sign_in.html', {
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

def ListSeasons(request):
    template = loader.get_template('seasons.html')
    seasons = Season.objects.all()
    context = RequestContext(request, {'seasons' : seasons, })
    return HttpResponse(template.render(context))

def SeazonUpdate(request, id=-1):
    us = None
    if id != -1:
        us = Season.objects.get(id=int(id))
    form = SeasonForm(request.POST or None, instance=us)
    if form.is_valid():
        form.save()
        return redirect('/seasons')
    else:
        return render_to_response('editform.html', RequestContext(request, {'formset': form}))

