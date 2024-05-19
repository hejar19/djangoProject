from django.db import models
from django.db.models.functions import datetime


# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False)
    numTel=models.CharField(max_length=10,null=False,blank=False)
    date = models.DateField(null=False,blank=False)
    #niveau = models.CharField(max_length=50,null=False,blank=False)
    seance = models.IntegerField(null=False,blank=False)
    montant = models.IntegerField(null=False,blank=False)
    paye = models.IntegerField(null=False,blank=False)
    NIVEAU_CHOICES = [
        ('CP', 'CP'),
        ('CE1', 'CE1'),
        ('CE2', 'CE2'),
        ('CM1', 'CM1'),
        ('CM2', 'CM2'),
        ('6eme', '6ème'),
        ('1AC', '1 AC'),
        ('2AC', '2 AC'),
        ('3AC', '3 AC'),
        ('tronc-commun', 'Tronc Commun'),
        ('premiere', 'Première année BAC'),
        ('deuxieme', 'Deuxième année BAC'),
    ]
    # Déclaration du champ niveau avec les choix définis
    niveau = models.CharField(max_length=20, choices=NIVEAU_CHOICES)


    def calculate_nonpaye(self):
        return self.montant - self.paye

class Professeur(models.Model):
    nom = models.CharField(max_length=200, null=False, blank=False)
    numTel = models.CharField(max_length=10, null=False, blank=False)
    #matiere = models.CharField(max_length=100, null=False, blank=False)
    nombre_heures = models.IntegerField(null=False, blank=False)
    MATIERE_CHOICES = [
        ('mathematiques', 'Mathématiques'),
        ('francais', 'Français'),
        ('arabe', 'Arabe'),
        ('anglais', 'Anglais'),
        ('histoire_geo', 'Histoire Géographie'),
        ('sciences', 'Sciences'),
        ('ei', 'Education Islamique'),
        ('philo', 'Philosohpie'),
    ]
    # Déclaration du champ matière avec les choix définis
    matiere = models.CharField(max_length=30, choices=MATIERE_CHOICES)


class Timetable(models.Model):
    DAYS_OF_WEEK = [
        ('Lundi', 'Lundi'),
        ('Mardi', 'Mardi'),
        ('Mercredi', 'Mercredi'),
        ('Jeudi', 'Jeudi'),
        ('Vendredi', 'Vendredi'),
        ('Samedi', 'Samedi'),
    ]

    PERIODS = [(str(i), str(i)) for i in range(1, 8)]

    SUBJECTS = [
        ('Mathématiques', 'Mathématiques'),
        ('Français', 'Français'),
        ('Arabe', 'Arabe'),
        ('Anglais', 'Anglais'),
        ('Histoire Géographie', 'Histoire Géographie'),
        ('Sciences', 'Sciences'),
        ('Education Islamique', 'Education Islamique'),
        ('Philosophie', 'Philosophie'),
    ]

    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    period = models.CharField(max_length=1, choices=PERIODS)
    subject = models.CharField(max_length=30, choices=SUBJECTS)

    class Meta:
        unique_together = ('day', 'period')

    def __str__(self):
        return f"{self.day} Period {self.period} - {self.subject}"