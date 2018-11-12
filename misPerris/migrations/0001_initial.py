# Generated by Django 2.1.2 on 2018-11-06 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='perro',
            fields=[
                ('id_perro', models.AutoField(max_length=5, primary_key=True, serialize=False)),
                ('foto', models.ImageField(null=True, upload_to='')),
                ('nombre_perro', models.CharField(max_length=30)),
                ('raza_predominante', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=30)),
                ('estado', models.CharField(choices=[('R', 'Rescatado'), ('D', 'Disponible'), ('A', 'adoptado')], default='R', max_length=1)),
            ],
        ),
    ]