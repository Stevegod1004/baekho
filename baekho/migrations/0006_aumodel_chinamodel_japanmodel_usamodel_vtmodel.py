# Generated by Django 2.2 on 2022-08-10 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baekho', '0005_auto_20220809_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ChinaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='JapanModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='USAModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='VtModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=20)),
                ('url', models.URLField()),
            ],
        ),
    ]
