# Generated by Django 4.0.5 on 2022-06-15 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_boleto_tenant_partido_tenant_usuario_tenant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partido',
            name='tenant',
        ),
    ]
