# Generated by Django 3.1 on 2020-08-26 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0008_auto_20200826_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets',
            name='petID',
            field=models.CharField(default='pet_1598446957.8474517', max_length=100),
        ),
        migrations.AlterField(
            model_name='pets',
            name='pet_details',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='demo.petsdetails'),
        ),
        migrations.AlterField(
            model_name='test',
            name='titel',
            field=models.CharField(default='hello1598446958', max_length=100),
        ),
    ]