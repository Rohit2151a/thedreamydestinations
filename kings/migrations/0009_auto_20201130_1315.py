# Generated by Django 3.1 on 2020-11-30 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kings', '0008_auto_20201129_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='location',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='phone',
            field=models.IntegerField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
