# Generated by Django 4.2.6 on 2024-03-04 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donwapp', '0005_article_image_students_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
    ]
