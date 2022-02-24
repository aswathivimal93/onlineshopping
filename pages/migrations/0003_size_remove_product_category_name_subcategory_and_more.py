# Generated by Django 4.0.2 on 2022-02-24 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_category_discount_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='category_name',
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('subcategory_image', models.ImageField(blank=True, null=True, upload_to='subcategory_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='pages.category')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='size', to='pages.size'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='subCategory',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='subCategory', to='pages.subcategory'),
            preserve_default=False,
        ),
    ]