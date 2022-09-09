# Generated by Django 3.1.3 on 2020-11-28 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=40)),
                ('pages', models.PositiveIntegerField(max_length=40)),
                ('price', models.FloatField(max_length=40)),
            ],
        ),
    ]