# Generated by Django 2.0.7 on 2019-04-04 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.TextField(default='This is cool'),
        ),
    ]
