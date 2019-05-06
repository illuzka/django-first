# Generated by Django 2.2.1 on 2019-05-06 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0012_chartticker_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('url', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=300)),
                ('body', models.CharField(max_length=1000)),
            ],
        ),
    ]
