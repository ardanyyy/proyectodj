# Generated by Django 2.1.1 on 2018-10-28 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_distribuidora_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Controles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Controles',
                'verbose_name_plural': 'Controles',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Plataformas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('Foto', models.ImageField(blank=True, null=True, upload_to='app', verbose_name='imagen')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('jubailidad', models.ManyToManyField(related_name='control', to='app.Controles', verbose_name='Controles')),
            ],
            options={
                'verbose_name': 'Plataforma',
                'verbose_name_plural': 'Plataformas',
                'ordering': ['-created'],
            },
        ),
        migrations.RemoveField(
            model_name='juego',
            name='Plataformas',
        ),
        migrations.AlterField(
            model_name='juego',
            name='distribuidora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keyd', to='app.Distribuidora'),
        ),
        migrations.AlterField(
            model_name='juego',
            name='genero',
            field=models.ManyToManyField(related_name='keygenero', to='app.Genero', verbose_name='Genero'),
        ),
        migrations.AddField(
            model_name='juego',
            name='plataformas',
            field=models.ManyToManyField(related_name='keyplat', to='app.Plataformas', verbose_name='Plataforma'),
        ),
    ]