# Generated by Django 3.2.3 on 2022-12-01 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0034_auto_20221201_2232'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Project',
            new_name='ProjectCount',
        ),
        migrations.RenameField(
            model_name='projectcount',
            old_name='Frontend',
            new_name='TotalNumberDynamicWebsite',
        ),
        migrations.RenameField(
            model_name='projectcount',
            old_name='FullWebsite',
            new_name='TotalNumberOfProject',
        ),
        migrations.RenameField(
            model_name='projectcount',
            old_name='Project',
            new_name='TotalNumberOfStaticWebsite',
        ),
    ]
