# Generated by Django 4.1.3 on 2023-02-18 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Codeflix', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='firstName',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='lastName',
        ),
    ]
