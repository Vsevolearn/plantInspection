# Generated by Django 3.0.8 on 2021-01-16 16:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, verbose_name='name')),
                ('Signature', models.CharField(max_length=200, verbose_name='signature')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Exemplar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, null=True, verbose_name='name')),
                ('Description', models.CharField(max_length=50000, verbose_name='description')),
                ('Model', models.FileField(upload_to='', verbose_name='model')),
                ('image', models.ImageField(upload_to='', verbose_name='image')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
            ],
            options={
                'verbose_name': 'exemplar',
                'verbose_name_plural': 'exemplar',
            },
        ),
        migrations.CreateModel(
            name='Genus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, verbose_name='name')),
            ],
            options={
                'verbose_name': 'genus',
                'verbose_name_plural': 'genus',
            },
        ),
        migrations.CreateModel(
            name='Protocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(default=datetime.date.today)),
                ('Address', models.CharField(max_length=200, verbose_name='address')),
                ('Сoordinates', models.CharField(max_length=200, verbose_name='coordinates')),
                ('Description', models.CharField(max_length=50000, verbose_name='description')),
                ('Archive', models.FileField(upload_to='', verbose_name='archive')),
                ('Сomments', models.CharField(max_length=50000, verbose_name='comments')),
                ('Genus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Genus')),
            ],
            options={
                'verbose_name': 'exemplar',
                'verbose_name_plural': 'exemplar',
            },
        ),
        migrations.CreateModel(
            name='ThreatExemplar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, verbose_name='name')),
                ('Exemplar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Exemplar')),
            ],
            options={
                'verbose_name': 'ThreatExemplar',
                'verbose_name_plural': 'ThreatExemplar',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, verbose_name='name')),
                ('Email', models.CharField(blank=True, default='', max_length=200, verbose_name='email')),
                ('Password', models.CharField(blank=True, default='', max_length=50, verbose_name='password')),
            ],
            options={
                'verbose_name': 'exemplar',
                'verbose_name_plural': 'exemplar',
            },
        ),
        migrations.CreateModel(
            name='ThreatExemplarImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='', verbose_name='image')),
                ('ThreatExemplar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ThreatExemplar')),
            ],
            options={
                'verbose_name': 'ThreatExemplarImage',
                'verbose_name_plural': 'ThreatExemplarImage',
            },
        ),
        migrations.CreateModel(
            name='ProtocolExemplarChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exemplar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Exemplar')),
                ('Protocol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Protocol')),
            ],
        ),
        migrations.AddField(
            model_name='protocol',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.User'),
        ),
        migrations.AddField(
            model_name='exemplar',
            name='Genus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Genus'),
        ),
    ]
