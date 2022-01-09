# Generated by Django 4.0 on 2021-12-20 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenditure',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='items', to='app.item'),
        ),
    ]