# Generated by Django 5.1.7 on 2025-04-03 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('token_blacklist', '0012_alter_outstandingtoken_user'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='Usuario',
        ),
    ]
