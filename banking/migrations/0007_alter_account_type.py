# Generated by Django 5.0.5 on 2024-05-23 15:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('banking', '0006_transaction_internal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='type',
            field=models.CharField(choices=[('savings', 'Savings'), ('checking', 'Checking')], default='savings',
                                   max_length=15),
        ),
    ]
