# Generated by Django 4.1.5 on 2023-01-30 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookingAPI', '0006_alter_booking_additional_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='additional_comments',
            field=models.TextField(default='If none, leave field as is', max_length=3000),
        ),
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=250),
        ),
        migrations.AlterField(
            model_name='booking',
            name='people',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
