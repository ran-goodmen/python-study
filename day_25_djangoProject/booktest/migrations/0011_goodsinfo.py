# Generated by Django 3.2 on 2023-06-12 14:21

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0010_pictest'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gcontent', tinymce.models.HTMLField()),
            ],
        ),
    ]
