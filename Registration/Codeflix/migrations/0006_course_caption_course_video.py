# Generated by Django 4.1.3 on 2023-03-22 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Codeflix', '0005_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='caption',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='video',
            field=models.FileField(default=' ', upload_to='video/%y'),
            preserve_default=False,
        ),
    ]
