# Generated by Django 4.2.1 on 2023-06-06 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0008_alter_alamatpengiriman_options_payment_order_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=70)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='produkitem',
            name='kategori',
            field=models.CharField(choices=[('S', 'Sayur'), ('B', 'Buah'), ('DS', 'Daging dan Seafood'), ('TO', 'Telur dan Olahan Susu')], max_length=2),
        ),
        migrations.AlterField(
            model_name='produkitem',
            name='label',
            field=models.CharField(choices=[('NEW', 'NEW'), ('SALE', 'SALE'), ('BEST', 'BEST')], max_length=4),
        ),
    ]
