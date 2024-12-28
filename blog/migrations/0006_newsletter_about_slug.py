# Generated by Django 5.1.1 on 2024-12-11 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_description_products_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='about',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]