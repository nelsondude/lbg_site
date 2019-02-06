# Generated by Django 2.1.5 on 2019-02-06 20:48

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0004_auto_20190128_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('contact_content', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2019, 2, 6, 20, 48, 11, 955966, tzinfo=utc)),
        ),
    ]
