# Generated by Django 2.2.5 on 2020-05-06 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dockerapi', '0021_imageinfo_is_ok'),
    ]

    operations = [
        migrations.CreateModel(
            name='SysConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('config_name', models.CharField(max_length=255, verbose_name='配置名称')),
                ('config_key', models.CharField(max_length=255, verbose_name='配置名称对应key')),
                ('config_value', models.TextField(default='', null=True, verbose_name='对应值')),
            ],
            options={
                'db_table': 'sys_config',
            },
        ),
    ]
