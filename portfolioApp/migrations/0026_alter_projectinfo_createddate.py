# Generated by Django 4.1 on 2022-08-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0025_research_paperlink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinfo',
            name='CreatedDate',
            field=models.DateField(null=True),
        ),
    ]