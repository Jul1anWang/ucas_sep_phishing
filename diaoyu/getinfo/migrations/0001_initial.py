# Generated by Django 3.0 on 2020-06-19 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40, verbose_name='username')),
                ('pwd', models.CharField(max_length=40, verbose_name='pwd')),
            ],
        ),
    ]
