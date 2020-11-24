# Generated by Django 3.1.3 on 2020-11-24 17:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('idKlient', models.AutoField(primary_key=True, serialize=False)),
                ('imie', models.CharField(max_length=100)),
                ('nazwisko', models.CharField(max_length=100)),
                ('nrtel', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pracownik',
            fields=[
                ('idPracownik', models.AutoField(primary_key=True, serialize=False)),
                ('imie', models.CharField(max_length=100)),
                ('nazwisko', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Specyfikacja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rabat', models.FloatField()),
                ('cena_sprzedazy', models.IntegerField()),
                ('ilosc', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Usluga',
            fields=[
                ('idUsluga', models.AutoField(primary_key=True, serialize=False)),
                ('nazwa', models.CharField(max_length=100)),
                ('cena_netto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Wizyta',
            fields=[
                ('idWizyta', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField(default=datetime.date.today)),
                ('godzina', models.TimeField(default=datetime.time)),
                ('klient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rezerwacje.klient')),
                ('pracownicy', models.ManyToManyField(to='Rezerwacje.Pracownik')),
                ('spec', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Rezerwacje.specyfikacja')),
                ('uslugi', models.ManyToManyField(to='Rezerwacje.Usluga')),
            ],
        ),
    ]
