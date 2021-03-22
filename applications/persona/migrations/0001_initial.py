# Generated by Django 3.1.6 on 2021-02-24 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0002_auto_20210223_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('job', models.CharField(choices=[('0', 'CONTADOR'), ('1', 'ADMINISTRADOR'), ('2', 'ECONOMISTA'), ('3', 'PROGRAMADOR'), ('4', 'OTRO')], max_length=1, verbose_name='Trabajo')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
            ],
        ),
    ]
