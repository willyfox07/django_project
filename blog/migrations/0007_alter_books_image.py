# Generated by Django 3.2.8 on 2021-11-02 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_books_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Обложка'),
        ),
    ]
