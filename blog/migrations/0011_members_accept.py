# Generated by Django 2.0.1 on 2018-05-20 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180519_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='accept',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
