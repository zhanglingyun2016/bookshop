# Generated by Django 2.0 on 2020-02-09 02:48

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
                ('phone', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=11)),
                ('age', models.CharField(max_length=11)),
                ('addtime', models.CharField(max_length=50)),
                ('logintime', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=500)),
            ],
        ),
    ]
