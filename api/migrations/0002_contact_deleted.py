# Generated by Django 3.2 on 2021-05-27 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Excluído'),
        ),
    ]
