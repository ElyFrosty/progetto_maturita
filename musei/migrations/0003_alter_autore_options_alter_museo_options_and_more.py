# Generated by Django 4.2.8 on 2024-05-13 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musei', '0002_opera_museo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autore',
            options={'verbose_name': 'Autore', 'verbose_name_plural': 'Autori'},
        ),
        migrations.AlterModelOptions(
            name='museo',
            options={'verbose_name': 'Museo', 'verbose_name_plural': 'Musei'},
        ),
        migrations.AlterModelOptions(
            name='opera',
            options={'verbose_name': 'Opera', 'verbose_name_plural': 'Opere'},
        ),
    ]
