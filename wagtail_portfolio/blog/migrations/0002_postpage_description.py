# Generated by Django 2.2.3 on 2019-07-26 22:30

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postpage',
            name='description',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
