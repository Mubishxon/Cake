# Generated by Django 5.1.1 on 2024-12-13 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_testimonial_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='image',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='testimonial',
            old_name='image',
            new_name='img',
        ),
    ]
