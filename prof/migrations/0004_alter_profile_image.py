# Generated by Django 4.1 on 2022-11-04 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='blank.png', height_field=300, upload_to='profile_images', width_field=300),
        ),
    ]
