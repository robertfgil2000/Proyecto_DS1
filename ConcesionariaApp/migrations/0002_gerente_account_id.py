# Generated by Django 4.2.1 on 2023-05-19 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GerenteApp', '0002_account_bossworkshop_account_id_seller_account_id'),
        ('ConcesionariaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gerente',
            name='account_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GerenteApp.account'),
        ),
    ]
