# Generated by Django 3.1.1 on 2020-09-07 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_dataset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='foodcat',
            field=models.CharField(choices=[('1', 'veg'), ('2', 'nonveg')], max_length=200),
        ),
    ]
