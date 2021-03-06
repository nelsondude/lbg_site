# Generated by Django 2.1.5 on 2019-02-15 19:12

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('home', '0005_auto_20190206_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricingsection',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2019, 2, 15, 19, 12, 6, 499758, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pricingsection',
            name='caption',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
