# Generated by Django 5.0.4 on 2024-05-01 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deteccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_caras', models.IntegerField(default=0)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
