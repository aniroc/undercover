# Generated by Django 3.0.2 on 2020-01-30 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200129_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qoh',
            field=models.IntegerField(default=0),
        ),
    ]
