# Generated by Django 3.2.13 on 2022-06-16 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact_message',
            new_name='Contact_emails',
        ),
        migrations.AlterModelOptions(
            name='contact_emails',
            options={'verbose_name_plural': 'Contact Emails'},
        ),
    ]