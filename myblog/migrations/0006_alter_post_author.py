# Generated by Django 3.2.7 on 2021-10-04 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_auto_20211002_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=255),
        ),
    ]