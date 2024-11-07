# Generated by Django 5.1.2 on 2024-11-07 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanificacionMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_trabajo', models.CharField(max_length=100)),
                ('refugio_trabajo', models.CharField(max_length=100)),
                ('tipos_tareas', models.CharField(max_length=100)),
                ('materiales', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='tipoparadero',
            name='area',
        ),
        migrations.RemoveField(
            model_name='seleccion',
            name='area',
        ),
        migrations.RemoveField(
            model_name='seleccion',
            name='materiales',
        ),
        migrations.RemoveField(
            model_name='seleccion',
            name='tareas',
        ),
        migrations.RemoveField(
            model_name='seleccion',
            name='tipo_paradero',
        ),
        migrations.CreateModel(
            name='OTFormulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('comuna', models.CharField(max_length=100)),
                ('tiempo_estimado', models.DurationField()),
                ('CECO', models.CharField(max_length=50)),
                ('jefe_proyecto', models.CharField(max_length=100)),
                ('supervisor', models.CharField(max_length=100)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('planificacion_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ot.planificacionmaterial')),
            ],
        ),
        migrations.DeleteModel(
            name='Area',
        ),
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.DeleteModel(
            name='Tarea',
        ),
        migrations.DeleteModel(
            name='Seleccion',
        ),
        migrations.DeleteModel(
            name='TipoParadero',
        ),
    ]
