# Generated by Django 2.0.1 on 2018-05-19 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_members_pbc_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='pbc_number',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
