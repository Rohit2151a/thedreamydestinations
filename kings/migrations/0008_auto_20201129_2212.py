# Generated by Django 3.1 on 2020-11-29 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kings', '0007_auto_20201129_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]
