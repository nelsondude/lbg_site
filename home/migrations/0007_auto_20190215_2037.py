# Generated by Django 2.1.5 on 2019-02-15 20:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190215_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='layout_lab_link',
        ),
        migrations.AddField(
            model_name='homepage',
            name='payments_link',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='announcement',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2019, 2, 15, 20, 37, 26, 998099, tzinfo=utc)),
        ),
    ]
