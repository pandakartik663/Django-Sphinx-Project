# Generated by Django 2.1.5 on 2019-04-12 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mcq', '0003_auto_20190404_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcqscore',
            name='usermcq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usermcq'),
        ),
    ]
