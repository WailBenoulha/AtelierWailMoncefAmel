# Generated by Django 4.2.1 on 2023-06-07 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_stock_qr_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr_codes/'),
        ),
    ]
