# Generated by Django 2.2.10 on 2020-04-05 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('description', models.TextField()),
                ('smtp', models.CharField(max_length=250)),
                ('port', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('tolist', models.CharField(max_length=250, null=True)),
                ('cclist', models.CharField(max_length=250, null=True)),
                ('bcclist', models.CharField(max_length=250, null=True)),
                ('is_deleted', models.CharField(default='0', max_length=1)),
            ],
        ),
    ]
