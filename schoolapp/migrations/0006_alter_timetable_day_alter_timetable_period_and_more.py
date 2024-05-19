# Generated by Django 5.0.4 on 2024-05-18 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0005_timetable_alter_professeur_matiere_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='day',
            field=models.CharField(choices=[('Lundi', 'Lundi'), ('Mardi', 'Mardi'), ('Mercredi', 'Mercredi'), ('Jeudi', 'Jeudi'), ('Vendredi', 'Vendredi'), ('Samedi', 'Samedi')], max_length=10),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='period',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=1),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject',
            field=models.CharField(choices=[('Mathématiques', 'Mathématiques'), ('Français', 'Français'), ('Arabe', 'Arabe'), ('Anglais', 'Anglais'), ('Histoire Géographie', 'Histoire Géographie'), ('Sciences', 'Sciences'), ('Education Islamique', 'Education Islamique'), ('Philosophie', 'Philosophie')], max_length=30),
        ),
        migrations.AlterUniqueTogether(
            name='timetable',
            unique_together={('day', 'period')},
        ),
    ]