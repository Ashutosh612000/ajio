# Generated by Django 4.2 on 2023-04-18 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_home_detail_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='home_detail',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
