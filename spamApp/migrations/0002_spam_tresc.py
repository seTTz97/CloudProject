# Generated by Django 3.2 on 2021-04-23 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spamApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spam',
            name='tresc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
