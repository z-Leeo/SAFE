# Generated by Django 4.2.1 on 2023-10-19 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='regCapacitacion',
            fields=[
                ('idregistro', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_completo', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('nombre_curso', models.CharField(max_length=100)),
                ('fecha_curso', models.DateField()),
                ('genero', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=10)),
                ('ubicacion_curso', models.CharField(max_length=100)),
                ('encargado_curso', models.CharField(max_length=100)),
                ('metodologia_ensenanza', models.CharField(choices=[('Presentaciones', 'Presentaciones'), ('Demostraciones', 'Demostraciones'), ('Ejercicios', 'Ejercicios Practicos'), ('Preguntas', 'Preguntas')], default='Presentaciones', max_length=100)),
                ('ciudad', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('codigo_postal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='regExamen',
            fields=[
                ('idregistro', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_completoE', models.CharField(default='', max_length=100)),
                ('rutE', models.CharField(max_length=100)),
                ('nombre_medicoE', models.CharField(max_length=100)),
                ('fecha_examenE', models.DateField()),
                ('generoE', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=10)),
                ('resultadoE', models.CharField(max_length=100)),
                ('observacionE', models.CharField(max_length=100)),
                ('servicio_atencionE', models.CharField(choices=[('Cardiologo', 'Cardiologo'), ('Odontologia', 'Odontologia'), ('Medicina General', 'Medicina General'), ('Traumatologia', 'Traumatologia'), ('Psicologia', 'Psicologia'), ('Dermatologia', 'Dermatologia')], default='Cardiologo', max_length=100)),
                ('historialE', models.CharField(max_length=80)),
                ('tratamientoE', models.CharField(max_length=50)),
                ('fecha_proxE', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='regMedico',
            fields=[
                ('idregistro', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_completoM', models.CharField(max_length=100)),
                ('rutM', models.CharField(max_length=100)),
                ('nombre_medicoM', models.CharField(max_length=100)),
                ('fecha_atencionM', models.DateField()),
                ('genero1', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=10)),
                ('previsionM', models.CharField(max_length=100)),
                ('ocupacionM', models.CharField(max_length=100)),
                ('servicio_atencionM', models.CharField(choices=[('Cardiologo', 'Cardiologo'), ('Odontologia', 'Odontologia'), ('Medicina General', 'Medicina General'), ('Traumatologia', 'Traumatologia'), ('Psicologia', 'Psicologia'), ('Dermatologia', 'Dermatologia')], default='Cardiologo', max_length=100)),
                ('historialM', models.CharField(max_length=80)),
                ('alergiaM', models.CharField(max_length=50)),
                ('fecha_proxM', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='regTerreno',
            fields=[
                ('idterreno', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_terreno', models.CharField(max_length=100)),
                ('ubicacion_terreno', models.CharField(max_length=100)),
                ('topografia', models.CharField(max_length=100)),
                ('fecha_registro', models.DateField()),
                ('riesgo1', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=10)),
                ('clima', models.CharField(max_length=100)),
                ('obsevacionT', models.CharField(max_length=100)),
                ('tipo_terreno', models.CharField(choices=[('Subterraneo', 'Subterraneo'), ('Superficie', 'Superficie'), ('Cantera', 'Cantera'), ('Montaña', 'Montaña')], default='Subterraneo', max_length=100)),
                ('deteccionQuimico', models.CharField(max_length=80)),
                ('materialUt', models.CharField(max_length=50)),
                ('salidas', models.CharField(max_length=100)),
            ],
        ),
    ]
