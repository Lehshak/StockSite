# Generated by Django 5.0.7 on 2024-07-24 19:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stocks", "0003_stock_average_volume_stock_beta_stock_current_ratio_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="stock",
            name="longBusinessSummary",
            field=models.CharField(default="No summary available", max_length=99999),
            preserve_default=False,
        ),
    ]