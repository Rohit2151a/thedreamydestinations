# Generated by Django 3.1 on 2020-12-20 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kings', '0010_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone1', models.IntegerField(max_length=10)),
                ('phone2', models.IntegerField(max_length=10)),
                ('date', models.CharField(max_length=100)),
                ('DestID', models.IntegerField(max_length=10)),
                ('destination', models.CharField(max_length=100)),
                ('From_place', models.CharField(max_length=100)),
                ('Days', models.IntegerField(max_length=10)),
                ('Nights', models.IntegerField(max_length=10)),
            ],
        ),
    ]
