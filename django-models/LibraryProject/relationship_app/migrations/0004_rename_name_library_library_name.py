# Generated by Django 4.2.19 on 2025-03-02 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0003_rename_author_name_author_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='library',
            old_name='name',
            new_name='library_name',
        ),
    ]
