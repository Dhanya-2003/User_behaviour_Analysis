# Generated by Django 3.2.16 on 2023-04-19 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_1', models.CharField(max_length=50)),
                ('field_2', models.IntegerField()),
                ('field_3', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
