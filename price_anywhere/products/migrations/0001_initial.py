# Generated by Django 4.2.7 on 2023-12-07 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upc', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('manufactor', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
