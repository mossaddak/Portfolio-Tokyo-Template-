# Generated by Django 4.1 on 2022-08-22 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0026_alter_projectinfo_createddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinfo',
            name='CreatedDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='research',
            name='PublishedDate',
            field=models.DateField(),
        ),
    ]
