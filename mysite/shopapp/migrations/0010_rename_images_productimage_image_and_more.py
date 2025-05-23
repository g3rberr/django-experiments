# Generated by Django 4.0.5 on 2025-04-21 22:04

from django.db import migrations, models
import shopapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0009_alter_product_preview_productimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='images',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='product',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to=shopapp.models.product_preview_derictory_path),
        ),
    ]
