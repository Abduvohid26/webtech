# Generated by Django 4.2.6 on 2024-03-04 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donwapp', '0004_article_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default=1, upload_to='article'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='students',
            name='image',
            field=models.ImageField(default=1, upload_to='students/'),
            preserve_default=False,
        ),
    ]
