# Generated by Django 4.1 on 2022-08-22 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0019_projectinfo_createddate'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectinfo',
            name='VideoLink',
            field=models.TextField(null=True),
        ),
    ]