# Generated by Django 3.2.4 on 2022-03-19 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=2038)),
                ('url_hash', models.PositiveIntegerField(db_index=True)),
                ('code', models.CharField(max_length=9)),
                ('code_hash', models.PositiveIntegerField(db_index=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]