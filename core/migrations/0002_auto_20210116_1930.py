# Generated by Django 3.0.8 on 2021-01-16 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exemplar',
            name='image',
        ),
        migrations.CreateModel(
            name='ProtocolExemplarFind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exemplar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Exemplar')),
                ('Protocol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Protocol')),
            ],
        ),
    ]