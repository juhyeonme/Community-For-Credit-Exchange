# Generated by Django 2.2.3 on 2019-07-22 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20190721_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='recommend',
            field=models.IntegerField(default=0, help_text='(updated on save)'),
        ),
        migrations.AlterField(
            model_name='review',
            name='assignment',
            field=models.IntegerField(choices=[(4, '적음'), ('없음', 5), (3, '보통'), (1, '헬')], default=5),
        ),
    ]
