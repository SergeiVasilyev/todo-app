# Generated by Django 3.2.7 on 2021-09-27 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='todoitem',
            field=models.CharField(max_length=800),
        ),
    ]
