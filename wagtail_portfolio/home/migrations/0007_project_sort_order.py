# Generated by Django 2.2.4 on 2019-08-25 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_homepage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]