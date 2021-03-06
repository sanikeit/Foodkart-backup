# Generated by Django 3.2.1 on 2021-05-09 23:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodkart', '0002_auto_20210509_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='restaurant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
