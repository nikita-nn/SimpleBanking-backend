# Generated by Django 5.0.5 on 2024-05-08 14:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('banking', '0002_account_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='internal',
            field=models.BooleanField(default=False),
        ),
    ]
