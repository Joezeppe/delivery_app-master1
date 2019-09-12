# Generated by Django 2.2.5 on 2019-09-11 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Monday', models.BooleanField()),
                ('Tuesday', models.BooleanField()),
                ('Wednesday', models.BooleanField()),
                ('Thursday', models.BooleanField()),
                ('Friday', models.BooleanField()),
                ('Saturday', models.BooleanField()),
                ('Sunday', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='kitchen')),
                ('days', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='kitchen.Days')),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('veg', models.BooleanField()),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('image', models.ImageField(blank=True, null=True, upload_to='kitchen')),
                ('kitchen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='kitchen.Kitchen')),
            ],
        ),
    ]