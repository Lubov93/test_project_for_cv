# Generated by Django 4.0.4 on 2022-05-24 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(default='images/default.png', max_length=200, upload_to='images/%Y/%m'),
        ),
    ]
