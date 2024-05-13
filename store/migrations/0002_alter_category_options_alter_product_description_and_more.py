# Generated by Django 4.2.2 on 2024-05-02 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='C:/Users/Intel/Downloads/'),
        ),
    ]