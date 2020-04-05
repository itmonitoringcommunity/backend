# Generated by Django 2.2.10 on 2020-04-05 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('description', models.TextField()),
                ('is_deleted', models.CharField(default='0', max_length=1)),
            ],
        ),
    ]
