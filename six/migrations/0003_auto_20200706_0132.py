# Generated by Django 3.0.6 on 2020-07-05 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('six', '0002_six_imagereason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='six',
            name='imagereason',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]