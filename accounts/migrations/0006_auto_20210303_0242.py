# Generated by Django 3.1.6 on 2021-03-03 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210302_1921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='auth_user',
            new_name='user',
        ),
    ]
