# Generated by Django 4.0 on 2021-12-18 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_expenditure_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenditure',
            name='mfs',
        ),
        migrations.DeleteModel(
            name='MFS',
        ),
    ]