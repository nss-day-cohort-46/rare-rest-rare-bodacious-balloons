# Generated by Django 3.2.3 on 2021-05-17 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rare_rest_api', '0002_alter_rareuser_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rareuser',
            name='profile_image_url',
            field=models.CharField(default='', max_length=250),
        ),
    ]
