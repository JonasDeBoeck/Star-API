# Generated by Django 3.0.8 on 2020-11-04 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20201104_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star',
            name='parallax',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]