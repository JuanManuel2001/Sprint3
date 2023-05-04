# Generated by Django 4.1.6 on 2023-05-04 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historia_clinica', '0003_alter_historiaclinica_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiaclinica',
            name='descripcion',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='historiaclinicaauditada',
            name='descripcion',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='medico',
            name='matricula',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='medicoauditado',
            name='matricula',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='apellido',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dni',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pacienteauditado',
            name='dni',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
