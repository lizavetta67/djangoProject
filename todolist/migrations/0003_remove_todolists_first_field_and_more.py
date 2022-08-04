# Generated by Django 4.1 on 2022-08-04 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_todolists_lastname_alter_todolists_third_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolists',
            name='first_field',
        ),
        migrations.RemoveField(
            model_name='todolists',
            name='second_field',
        ),
        migrations.RemoveField(
            model_name='todolists',
            name='third_field',
        ),
        migrations.AddField(
            model_name='todolists',
            name='email',
            field=models.EmailField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='todolists',
            name='firstname',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='todolists',
            name='username',
            field=models.CharField(default='', max_length=64),
        ),
    ]