# Generated by Django 2.2.5 on 2019-09-11 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0003_auto_20190911_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='dish/'),
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='kitchen/'),
        ),
    ]
