# Generated by Django 5.0.6 on 2024-06-24 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stqcapp', '0004_remove_dispatchform_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispatchform',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
