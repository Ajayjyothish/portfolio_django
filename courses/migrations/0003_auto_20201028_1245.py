# Generated by Django 3.1.2 on 2020-10-28 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20201028_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
