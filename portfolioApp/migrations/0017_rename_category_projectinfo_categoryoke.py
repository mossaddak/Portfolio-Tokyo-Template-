# Generated by Django 4.1 on 2022-08-19 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0016_rename_category_projectinfo_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectinfo',
            old_name='category',
            new_name='categoryOke',
        ),
    ]
