# Generated by Django 3.1.6 on 2021-02-16 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zapatillasApp', '0002_marca'),
    ]

    operations = [
        migrations.AddField(
            model_name='zapatilla',
            name='marcaPerteneciente',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='zapatillasApp.marca'),
        ),
    ]
