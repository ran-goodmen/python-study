# Generated by Django 3.2 on 2023-06-05 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0004_bookinfo_bprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='bprice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
