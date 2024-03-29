from django.http import HttpResponse
from django.template import loader, RequestContext
from main.forms import SeasonForm
from main.models import *
from datetime import datetime
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.sessions.models import Session
from main.forms import *
from django.shortcuts import render_to_response, redirect

def signUp(request):
    if request.method == 'POST': # If the form has been submitted
        form = UserFormSignUp(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = UserFormSignUp() # An unbound form
    
    return render(request, 'signUp.html', {
        'formset': form,
    })


def signIn(request):
    if request.method == 'POST':
        form = UserFormSignIn(request.POST)
        try:
            us = User.objects.get(login=form.data['login'],password=form.data['password'])
        except:
            return redirect('/logowanie')
        request.session.set_expiry(60) #ustawienie wygasniecia sesji po 6o sekundach
        request.session['user'] = us.id
        request.session['login'] = us.login
        request.session['type'] = us.type
        return redirect('/')
    else:
        form = UserFormSignIn()
        return render_to_response('signIn.html', RequestContext(request, {'formset': form}))


def logout(request):
    del request.session["user"]
    del request.session["login"]
    del request.session["type"]
    request.session.modified = True
    return redirect('/')


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

def player(request, player_id, team_id):
    template = loader.get_template('player.html')
    team = Team.objects.get(id=int(team_id))
    player = Player.objects.get(id=int(player_id))
    context = RequestContext(request, {'player' : player, 'team': team, })
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

def delSeason(request, id):
    Season.objects.get(id=int(id)).delete()
    return redirect('/seasons')

def ListReasons(request, id):
    template = loader.get_template('rounds.html')
    seasons = Season.objects.get(id=int(id))
    rounds = Round.objects.filter(s_id=seasons)
    context = RequestContext(request, {'rounds' : rounds, })
    return HttpResponse(template.render(context))


def RoundUpdate(request, id=-1):
    us = None
    if id != -1:
        us = Round.objects.get(id=int(id))
    form = RoundForm(request.POST or None, instance=us)
    if form.is_valid():
        form.save()
        return redirect('/seasons')
    else:
        return render_to_response('editform.html', RequestContext(request, {'formset': form}))

def delRound(request, id):
    Round.objects.get(id=int(id)).delete()
    return redirect('/seasons')

def coach(request):
    coach = Coach.objects.all()
    if request.method == 'POST':
        form = CoachForm(request.POST)
        if form.is_valid():
            form.save()
    else: 
        form = CoachForm() 
    return render(request, 'coach.html', {
        'form': form, 'coach': coach,
    })
    
def CoachUpdate(request, id=-1):
    us = None
    if id != -1:
        us = Coach.objects.get(id=int(id))
    form = CoachForm(request.POST or None, instance=us)
    if form.is_valid():
        form.save()
    return redirect('/coach')

def CoachDelete(request, id):
    Coach.objects.get(id=int(id)).delete()
    return redirect('/coach')

def teams(request):
    teams = Team.objects.all()
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
    else: 
        form = TeamForm() 
    return render(request, 'teams.html', {
        'form': form, 'teams': teams,
    })
    
def TeamUpdate(request, id=-1):
    us = None
    if id != -1:
        us = Team.objects.get(id=int(id))
    form = TeamForm(request.POST or None, instance=us)
    if form.is_valid():
        form.save()
    return redirect('/teams')

def TeamDelete(request, id):
    Team.objects.get(id=int(id)).delete()
    return redirect('/teams')
    
def players(request):
    players = Player.objects.all()
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
    else: 
        form = PlayerForm() 
    return render(request, 'players.html', {
        'form': form, 'players': players,
    })
    
def PlayerUpdate(request, id=-1):
    us = None
    if id != -1:
        us = Player.objects.get(id=int(id))
    form = PlayerForm(request.POST or None, instance=us)
    if form.is_valid():
        form.save()
    return redirect('/players')

def PlayerDelete(request, id):
    Player.objects.get(id=int(id)).delete()
    return redirect('/players')
