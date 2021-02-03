# Generated by Django 3.1.5 on 2021-02-02 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20210202_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='pizza',
        ),
        migrations.AddField(
            model_name='pizza',
            name='order',
            field=models.ForeignKey(default=-2021, on_delete=django.db.models.deletion.CASCADE, to='order.order'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
