# Generated by Django 4.0.3 on 2022-06-26 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='startexam',
            old_name='exam',
            new_name='examType',
        ),
        migrations.AddField(
            model_name='startexam',
            name='subject',
            field=models.CharField(default='USE OF ENGLISH', max_length=20),
        ),
    ]
