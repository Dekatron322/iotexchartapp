# Generated by Django 3.1.7 on 2021-12-11 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptodata',
            name='date',
            field=models.CharField(default='Crypto Data', max_length=500),
        ),
    ]
