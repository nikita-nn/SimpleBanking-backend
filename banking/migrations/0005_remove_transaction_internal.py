# Generated by Django 5.0.5 on 2024-05-08 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0004_alter_account_account_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='internal',
        ),
    ]
