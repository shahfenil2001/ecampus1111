# Generated by Django 4.0.3 on 2022-03-03 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BatchDetails',
            new_name='BatchDetail',
        ),
        migrations.AlterModelOptions(
            name='batch',
            options={'verbose_name_plural': 'Batch'},
        ),
        migrations.AlterModelOptions(
            name='batchdetail',
            options={'verbose_name_plural': 'BatchDetails'},
        ),
        migrations.AlterModelOptions(
            name='batchtime',
            options={'verbose_name_plural': 'BatchTime'},
        ),
    ]
