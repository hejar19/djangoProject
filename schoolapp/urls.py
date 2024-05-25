from django.urls import path
from schoolapp import views
from .forms import CustomAuthenticationForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('add/', views.addStudent, name='registration'),
    path('bar/', views.sidebar, name='sidebar'),
    path('list/', views.list, name='list'),
    path('recherche/', views.rechStudent, name='recherche'),
    path('modif/', views.modifStudent, name='modif'),
    # path('process_data/', views.process_data, name='process_data'),
    path('listProf/', views.listProf, name='listProf'),
    path('addProf/', views.addProf, name='addProf'),
    path('suppStudent/', views.suppStudent, name='suppStudent'),
    path('suppProf/', views.suppProf, name='suppProf'),
    path('modify/<int:student_id>/', views.modify_student, name='modify_student'),
    path('confirmation_professeur/', views.confirmation_professeur, name='confirmation_professeur'),
    path('confirmation_student/', views.confirmation_student, name='confirmation_student'),
    path('rechercheProf/', views.rechercheProf, name='rechercheProf'),
    path('modifyProf/<int:professeur_id>/', views.modifyProf, name='modifyProf'),
    path('modifProf/', views.modifProf, name='modifProf'),
    path('confirmationModifProf/', views.confirmationModifProf, name='confirmModifProf'),
    path('confirmationModifStudent/', views.confirmationModifStudent, name='confirmModifStudent'),
    path('timetable/', views.timetable, name='timetable'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
