# Generated by Django 4.1 on 2022-08-24 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0029_contact_createddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='CreatedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
