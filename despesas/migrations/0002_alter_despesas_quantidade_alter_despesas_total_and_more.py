# Generated by Django 4.0.4 on 2022-06-16 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesas',
            name='Quantidade',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100, verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='despesas',
            name='Total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100, verbose_name='Total'),
        ),
        migrations.AlterField(
            model_name='despesas',
            name='Valor',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100, verbose_name='Valor'),
        ),
    ]