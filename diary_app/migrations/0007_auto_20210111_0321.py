# Generated by Django 3.1.4 on 2021-01-11 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary_app', '0006_auto_20210105_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaryentry',
            name='title',
            field=models.CharField(max_length=264),
        ),
    ]
