# Generated by Django 2.1.8 on 2019-07-16 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0005_auto_20190716_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='school',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='schoolId',
            field=models.CharField(max_length=50),
        ),
    ]
