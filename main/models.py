from django.db import models

class Season(models.Model):
    year = models.IntegerField()
    

class Coach(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    

class Round(models.Model):
    type = models.BooleanField()
    s_id = models.ForeignKey(Season)
    

class Team(models.Model):
    name = models.CharField(max_length=32)
    c_id = models.ForeignKey(Coach)
    

class Player(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    number = models.IntegerField()
    t_id = models.ForeignKey(Team)
    

class Matchday(models.Model):
    start = models.DateField()
    end = models.DateField()
    r_id = models.ForeignKey(Round)
    

class Match(models.Model):
    data = models.DateField()
    m_id = models.ForeignKey(Matchday)
    home_id = models.ForeignKey(Team, related_name= 'match_home_id')
    away_id = models.ForeignKey(Team, related_name= 'match_away_id')
    

class MatchPlayer(models.Model):
    m_id = models.ForeignKey(Match)
    p_id = models.ForeignKey(Player)
    

class EventType(models.Model):
    name = models.CharField(max_length=32)
    

class Event(models.Model):
    type = models.ForeignKey(EventType)
    p_id = models.ForeignKey(Player)
    m_id = models.ForeignKey(Match)
    t_id = models.ForeignKey(Team)
    
    
class User(models.Model):
    login = models.CharField(max_length=32, unique=True)
    email = models.EmailField(max_length=32)
    password = models.CharField(max_length=32)
    USER = 'USR'
    ADMIN = 'ADM'
    MODERATOR = 'MOD'
    TYPE_CHOICES = (
        (USER, 'uzytkownik'),
        (ADMIN, 'admin'),
        (MODERATOR, 'moderator')
    )
    type = models.CharField(max_length=3,
                                      choices=TYPE_CHOICES,
                                      default=USER)
    ban = models.BooleanField(default=False) 

