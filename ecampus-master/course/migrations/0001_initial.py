# Generated by Django 4.0.2 on 2022-02-28 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseId', models.IntegerField(primary_key=True, serialize=False)),
                ('courseName', models.CharField(max_length=50)),
                ('courseDescription', models.TextField()),
                ('active', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0)),
            ],
        ),
    ]