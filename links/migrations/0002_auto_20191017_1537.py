# Generated by Django 2.2.6 on 2019-10-17 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='descritpion',
            new_name='description',
        ),
    ]