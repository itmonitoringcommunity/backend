# Generated by Django 2.2.10 on 2020-04-05 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0002_auto_20200405_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
