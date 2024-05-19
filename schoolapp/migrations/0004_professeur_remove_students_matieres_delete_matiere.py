# Generated by Django 5.0.4 on 2024-05-12 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0003_matiere_students_matieres'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('numTel', models.CharField(max_length=10)),
                ('matiere', models.CharField(max_length=100)),
                ('nombre_heures', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='students',
            name='matieres',
        ),
        migrations.DeleteModel(
            name='Matiere',
        ),
    ]
