# Generated by Django 4.1.3 on 2022-11-15 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ferretic', '0009_alter_user_employee_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_product_quantity', models.IntegerField()),
                ('order_subtotal', models.IntegerField()),
                ('order_total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_date', models.DateTimeField(auto_now_add=True)),
                ('invoice_product_quantity', models.IntegerField()),
                ('invoice_subtotal', models.IntegerField()),
                ('invoice_total', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='order_product',
            name='order',
        ),
        migrations.RemoveField(
            model_name='order_product',
            name='product',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='client',
            new_name='client_id',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='employee',
            new_name='employee_id',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='employee',
            new_name='employee_id',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='vendor',
            new_name='vendor_id',
        ),
        migrations.DeleteModel(
            name='Invoice_product',
        ),
        migrations.DeleteModel(
            name='Order_product',
        ),
        migrations.AddField(
            model_name='sold',
            name='invoice_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ferretic.invoice'),
        ),
        migrations.AddField(
            model_name='sold',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ferretic.product'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ferretic.order'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ferretic.product'),
        ),
    ]
