# Generated by Django 3.0.8 on 2020-11-29 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('star_system', models.CharField(max_length=30)),
                ('distance', models.FloatField()),
                ('year_of_discovery', models.IntegerField(blank=True, default=None, null=True)),
                ('apparent_magnitude', models.FloatField(blank=True, default=None, null=True)),
                ('absolut_magnitude', models.FloatField(blank=True, default=None, null=True)),
                ('spectral_class', models.CharField(choices=[('O', 'O'), ('B', 'B'), ('A', 'A'), ('F', 'F'), ('G', 'G'), ('K', 'K'), ('M', 'M'), ('L', 'L'), ('T', 'T'), ('Y', 'Y')], max_length=1)),
                ('parallax', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
    ]
