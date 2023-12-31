# Generated by Django 4.2.4 on 2023-09-03 08:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hw_app', '0002_alter_order_common_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date_registration',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='goods',
            name='date_adding',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_create',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
