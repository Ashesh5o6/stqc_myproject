# Generated by Django 5.0.6 on 2024-06-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Designation', models.CharField(max_length=30)),
                ('Username', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
    ]
