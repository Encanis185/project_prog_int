# Generated by Django 3.2.8 on 2021-11-23 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20211122_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]