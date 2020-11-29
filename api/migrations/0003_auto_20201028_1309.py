# Generated by Django 3.0.8 on 2020-10-28 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201028_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star',
            name='absolute_magnitude',
            field=models.FloatField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='star',
            name='apparent_magnitude',
            field=models.FloatField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='star',
            name='year_of_discovery',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
