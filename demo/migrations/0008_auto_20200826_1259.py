# Generated by Django 3.1 on 2020-08-26 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('demo', '0007_auto_20200826_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets',
            name='petID',
            field=models.CharField(default='pet_1598446772.2279384', max_length=100),
        ),
        migrations.AlterField(
            model_name='pets',
            name='petUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='test',
            name='titel',
            field=models.CharField(default='hello1598446772', max_length=100),
        ),
    ]
