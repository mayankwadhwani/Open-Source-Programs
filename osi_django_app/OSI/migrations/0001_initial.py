# Generated by Django 2.2.1 on 2019-05-10 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='osc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('osc_homepage', models.URLField(default=None)),
                ('awards', models.CharField(max_length=50)),
                ('timeline', models.URLField(blank=True)),
                ('publish', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='soc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('soc_homepage', models.URLField(default=None)),
                ('stripend', models.BooleanField(default=False)),
                ('timeline', models.URLField(blank=True)),
                ('publish', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='univ_soc_woc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('homepage', models.URLField(default=None)),
                ('awards', models.CharField(max_length=50)),
                ('timeline', models.URLField(blank=True)),
                ('publish', models.BooleanField(default=False)),
            ],
        ),
    ]
