# Generated by Django 3.1 on 2020-08-26 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0010_auto_20200826_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pets',
            name='petID',
        ),
        migrations.AddField(
            model_name='petsdetails',
            name='petID',
            field=models.CharField(default='pet_15984474172867162', max_length=100),
        ),
        migrations.AlterField(
            model_name='test',
            name='titel',
            field=models.CharField(default='hello1598447417', max_length=100),
        ),
    ]
