# Generated by Django 2.0.1 on 2018-05-20 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20180520_1137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='accept',
            new_name='Agree_to_Terms_and_Conditions',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='fname',
            new_name='First_Name',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='gender',
            new_name='Gender',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='faculty',
            new_name='Interested_PBC_Faculty',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='lname',
            new_name='Last_Name',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='mnumber',
            new_name='Mobile_Number',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='nationality',
            new_name='Nationality',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='occupation',
            new_name='Occupation',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='title',
            new_name='Title',
        ),
    ]