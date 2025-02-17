# Generated by Django 2.2.14 on 2020-08-04 02:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('edunext_paypal_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paypal',
            name='ipn_notification',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paypal',
            name='item_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paypal',
            name='mc_currency',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paypal',
            name='notify_version',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paypal',
            name='payer_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paypal',
            name='payment_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='paypal',
            name='payment_gross',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paypal',
            name='payment_status',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paypal',
            name='receiver_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paypal',
            name='shipping',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paypal',
            name='txn_checkout',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paypal',
            name='verify_sign',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paypal',
            name='protection_eligibility',
            field=models.CharField(max_length=50),
        ),
    ]
