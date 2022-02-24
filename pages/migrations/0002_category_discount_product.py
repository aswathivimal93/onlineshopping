# Generated by Django 4.0.2 on 2022-02-23 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=1500)),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='category_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('desc', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('desc', models.CharField(max_length=1500)),
                ('price', models.FloatField()),
                ('image_link1', models.ImageField(blank=True, null=True, upload_to='Product_images/')),
                ('image_link2', models.ImageField(blank=True, null=True, upload_to='Product_images/')),
                ('image_link3', models.ImageField(blank=True, null=True, upload_to='Product_images/')),
                ('created_at', models.DateField()),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='pages.category')),
                ('discount_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discount', to='pages.discount')),
            ],
        ),
    ]