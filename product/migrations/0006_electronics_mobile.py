# Generated by Django 4.2 on 2023-04-19 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_grocery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Electronics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electronic_item', models.CharField(max_length=50)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product_list')),
            ],
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('mobile_model', models.CharField(max_length=50)),
                ('electronic_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.electronics')),
            ],
        ),
    ]
