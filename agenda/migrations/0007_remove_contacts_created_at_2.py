# Generated by Django 5.0.4 on 2024-04-26 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0006_remove_friendsrequest_user_id_contacts_created_at_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='created_at_2',
        ),
    ]
