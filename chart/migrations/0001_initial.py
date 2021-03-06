# Generated by Django 2.2 on 2019-04-21 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('price_labels', models.TextField()),
                ('price_margins', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ChartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_margin_top', models.FloatField()),
                ('item_height', models.FloatField()),
                ('shadow_uheight', models.FloatField()),
                ('shadow_dheight', models.FloatField()),
                ('margin_left_value', models.FloatField()),
                ('volume', models.FloatField()),
                ('date', models.DateTimeField()),
                ('number_of_items', models.IntegerField()),
                ('updown_item', models.IntegerField()),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chart.Ticker')),
            ],
        ),
    ]
