# Generated by Django 3.0.8 on 2020-07-21 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='title', max_length=100)),
                ('description', models.TextField(db_column='description', max_length=1000)),
                ('author', models.CharField(db_column='author', max_length=100)),
                ('year', models.IntegerField(db_column='year', default=2000)),
            ],
        ),
    ]
