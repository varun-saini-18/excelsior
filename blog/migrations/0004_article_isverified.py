# Generated by Django 2.2.13 on 2020-06-09 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200609_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='isVerified',
            field=models.BooleanField(default=False),
        ),
    ]