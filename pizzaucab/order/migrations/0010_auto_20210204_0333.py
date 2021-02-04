# Generated by Django 3.1.6 on 2021-02-04 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_auto_20210203_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='total',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pizza',
            name='ingredient',
            field=models.ManyToManyField(blank=True, to='order.Ingredient'),
        ),
    ]