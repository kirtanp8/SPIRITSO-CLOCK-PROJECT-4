# Generated by Django 3.2.9 on 2021-12-21 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20211221_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='fibre',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10),
        ),
    ]