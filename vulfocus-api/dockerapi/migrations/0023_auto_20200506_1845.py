# Generated by Django 2.2.5 on 2020-05-06 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dockerapi', '0022_sysconfig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sysconfig',
            name='config_key',
            field=models.CharField(max_length=255, unique=True, verbose_name='配置名称对应key'),
        ),
    ]
