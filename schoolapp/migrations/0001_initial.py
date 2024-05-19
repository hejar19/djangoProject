# Generated by Django 5.0.4 on 2024-04-20 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('numTel', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('niveau', models.IntegerField()),
                ('seance', models.IntegerField()),
                ('montant', models.IntegerField()),
                ('paye', models.IntegerField()),
            ],
        ),
    ]
