# Generated by Django 4.2 on 2023-04-17 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=10)),
                ('Date_of_birth', models.DateField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]