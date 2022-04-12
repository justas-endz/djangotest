# Generated by Django 4.0.4 on 2022-04-12 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('krautuve', '0004_order_product_id_alter_order_status_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productorder',
            name='product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='krautuve.product', verbose_name='Product'),
        ),
    ]
