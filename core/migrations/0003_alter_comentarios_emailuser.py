# Generated by Django 3.2.5 on 2021-09-04 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_emailusar_comentarios_emailuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='EmailUser',
            field=models.EmailField(max_length=50),
        ),
    ]
