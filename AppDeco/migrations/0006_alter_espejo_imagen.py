# Generated by Django 5.0.1 on 2024-01-24 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDeco', '0005_lampara_imagen_alter_sillon_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espejo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]