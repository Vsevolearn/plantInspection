# Generated by Django 3.0.8 on 2021-01-16 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210116_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='exemplar',
            name='image',
            field=models.ImageField(default=2, upload_to='', verbose_name='image'),
            preserve_default=False,
        ),
    ]