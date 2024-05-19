import json
from datetime import datetime
from itertools import zip_longest

from babel.dates import format_date
from django.core.mail.backends import console
from django.db.models import Q
from django.db.models.functions import Lower
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from schoolapp.forms import TimetableForm
from schoolapp.models import Students, Professeur, Timetable


# Create your views here.
def sidebar(request):
    return render(request, 'acceuil.html')
def confirmation_student(request):
    return render(request, 'confirmationAjoutStudent.html')

def addStudent(request):
    if request.method == 'POST':
        # print("Données de la requête POST :", request.POST)
        # Récupérer les données du formulaire
        name = request.POST.get('name')
        numTel = request.POST.get('numTel')
        #date = request.POST.get('date')
        date_str = request.POST.get('date')  # Déclaration de la variable date_str
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        niveau = request.POST.get('niveau')
        seance = request.POST.get('seance')
        montant = request.POST.get('montant')
        paye = request.POST.get('paye')

        # Créer une nouvelle instance de la classe Students et enregistrer les données
        new_student = Students(name=name, numTel=numTel, date=date, niveau=niveau, seance=seance, montant=montant,
                               paye=paye)
        new_student.save()
        # Enregistrer les matières sélectionnées avec le nouvel étudiant


        # Rediriger vers une autre page ou rendre une page de confirmation
        return render(request, 'confirmationAjoutStudent.html')

    # Si la méthode de la requête n'est pas POST, afficher simplement le formulaire
    return render(request, 'addStudent.html')

def list(request):
    students = Students.objects.all()
    for student in students:
        student.nonpaye = student.montant - student.paye
        # Ajoutez ceci pour obtenir le texte du niveau pour chaque étudiant
        student.niveau_text = dict(Students.NIVEAU_CHOICES).get(student.niveau)
    return render(request, 'listStudents.html', {'students': students})
def modifStudent(request):
    students = Students.objects.all()
    for student in students:
        student.nonpaye = student.montant - student.paye
        student.niveau_text = dict(Students.NIVEAU_CHOICES).get(student.niveau)
    return render(request, 'modifStudent.html', {'students': students})
def modify_student(request, student_id):
    student = Students.objects.get(id=student_id)
    if request.method == 'POST':
        print(request.POST)  # Ajout pour vérifier les données du formulaire
        date_str = request.POST.get('date')  # Déclaration de la variable date_str
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        student.name = request.POST['name']
        student.numTel = request.POST['numTel']
        student.date = date
        student.niveau = request.POST['niveau']
        student.seance = request.POST['seance']
        student.montant = request.POST['montant']
        student.paye = request.POST['paye']
        student.save()
        return redirect('confirmModifStudent')
    student.niveau_text = dict(Students.NIVEAU_CHOICES).get(student.niveau)
    return render(request, 'fiche.html', {'student': student})
def confirmationModifStudent(request):
    return render(request, 'confirmModifStudent.html')

def suppStudent(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')  # Obtenez l'ID de l'étudiant à supprimer
        student = Students.objects.get(id=student_id)
        student.delete()  # Supprimez l'étudiant de la base de données
        return redirect(
            'suppStudent')  # Redirigez l'utilisateur vers la page de liste des étudiants après la suppression
    students = Students.objects.all()
    for student in students:
        student.nonpaye = student.montant - student.paye
        student.niveau_text = dict(Students.NIVEAU_CHOICES).get(student.niveau)
    return render(request, 'suppStudent.html', {'students': students})
def rechStudent(request):
    if request.method == 'POST':
        nom_recherche = request.POST.get('nameRech')
        # Recherche des étudiants dont le nom contient la chaîne recherchée
        students = Students.objects.filter(Q(name__icontains=nom_recherche))
        if students.exists():
            # Calculer nonpaye pour chaque étudiant
            for student in students:
                student.nonpaye = student.montant - student.paye
                student.niveau_text = dict(Students.NIVEAU_CHOICES).get(student.niveau)
            return render(request, 'recherche.html', {'students': students, 'nom_recherche': nom_recherche})
        else:
            # Si aucun étudiant correspondant n'est trouvé, renvoyer un message d'erreur
            erreur = "Aucune adhérente trouvée avec ce nom."
            return render(request, 'recherche.html', {'erreur': erreur})
    return render(request, 'recherche.html')


def listProf(request):
    professeurs = Professeur.objects.all()
    return render(request, 'listProf.html', {'professeurs': professeurs})

def confirmation_professeur(request):
    return render(request, 'confirmationAjoutProf.html')

def addProf(request):
        if request.method == 'POST':
            # Récupérer les données du formulaire
            nom = request.POST.get('nom')
            numTel = request.POST.get('numTel')
            matiere = request.POST.get('matiere')
            nombre_heures = request.POST.get('nombre_heures')

            # Créer une nouvelle instance de la classe Professeur et enregistrer les données
            nouveau_professeur = Professeur(nom=nom, numTel=numTel, matiere=matiere, nombre_heures=nombre_heures)
            nouveau_professeur.save()

            # Rediriger vers une autre page ou rendre une page de confirmation
            return redirect('confirmation_professeur')

        # Si la méthode de la requête n'est pas POST, afficher simplement le formulaire
        return render(request, 'addProf.html')




def suppProf(request):
    if request.method == 'POST':
        professeur_id = request.POST.get('professeur_id')  # Obtenir l'ID du professeur à supprimer
        professeur = Professeur.objects.get(id=professeur_id)
        professeur.delete()  # Supprimer le professeur de la base de données
        return redirect('listProf')  # Rediriger l'utilisateur vers la page de liste des professeurs après la suppression

    professeurs = Professeur.objects.all()
    return render(request, 'suppProf.html', {'professeurs': professeurs})

def modifyProf(request, professeur_id):
    professeur = Professeur.objects.get(id=professeur_id)
    if request.method == 'POST':
        #print(request.POST)  # Ajout pour vérifier les données du formulaire
        professeur.nom = request.POST['nom']
        professeur.numTel = request.POST['numTel']
        professeur.matiere = request.POST['matiere']
        professeur.nombre_heures = request.POST['nombre_heures']
        professeur.matiere_text = dict(Professeur.MATIERE_CHOICES).get(professeur.matiere)
        professeur.save()
        return redirect('confirmModifProf')
    professeur.matiere_text = dict(Professeur.MATIERE_CHOICES).get(professeur.matiere)
    return render(request, 'ficheProf.html', {'professeur': professeur})
def modifProf(request):
    professeurs = Professeur.objects.all()
    return render(request, 'modifProf.html', {'professeurs': professeurs})

def confirmationModifProf(request):
    return render(request, 'confirmModifProf.html')

def rechercheProf(request):
    if request.method == 'POST':
        nom_recherche = request.POST.get('nameRech')
        professeurs = Professeur.objects.filter(nom__icontains=nom_recherche)
        if not professeurs:
            erreur = "Aucun professeur trouvé avec ce nom."
            return render(request, 'rechercheProf.html', {'erreur': erreur})
        else:
            return render(request, 'rechercheProf.html', {'professeurs': professeurs, 'nom_recherche': nom_recherche})
    else:
        return render(request, 'rechercheProf.html')


def timetable(request):
    print("ok")
    timetable_entries = Timetable.objects.all()
    days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi']
    periods = [str(i) for i in range(1, 8)]

    timetable = {day: {period: '' for period in periods} for day in days}
    for entry in timetable_entries:
        timetable[entry.day][entry.period] = entry.subject

    if request.method == 'POST':
        form = TimetableForm(request.POST)
        if form.is_valid():
            day = form.cleaned_data['day']
            period = form.cleaned_data['period']
            subject = form.cleaned_data['subject']
            print("Day:", day)
            print("Period:", period)
            print("Subject:", subject)

            # Met à jour ou crée une nouvelle entrée
            #timetable_entry, created = Timetable.objects.update_or_create(day=day, period=period, defaults={'subject': subject})
            #print("Entry created:", created)
            # Met à jour ou crée une nouvelle entrée
            Timetable.objects.update_or_create(day=day, period=period, defaults={'subject': subject})
            return redirect('timetable')
    else:
        print("impossible")
        form = TimetableForm()

    context = {
        'timetable': timetable,
        'form': form,
    }
    return render(request, 'acceuil.html', context)
