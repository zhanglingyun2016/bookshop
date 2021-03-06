# Generated by Django 2.0 on 2020-02-10 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booktype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('pid', models.IntegerField()),
                ('path', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=160),
        ),
    ]
