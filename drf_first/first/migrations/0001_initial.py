# Generated by Django 2.0.6 on 2020-10-27 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.SmallIntegerField(choices=[(0, 'male'), (1, 'famale'), (2, 'other')], default=0)),
            ],
            options={
                'db_table': 'user_brf',
            },
        ),
    ]