# Generated by Django 4.0.4 on 2022-06-23 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emotionhistoric',
            name='emotion_percentage',
            field=models.DecimalField(decimal_places=4, max_digits=7),
        ),
    ]