# Generated by Django 3.2.8 on 2021-11-02 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_books_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='review',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Рецензия'),
        ),
    ]