# Generated by Django 3.2.10 on 2021-12-11 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0002_alter_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=122),
        ),
    ]
