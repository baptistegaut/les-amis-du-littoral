# Generated by Django 2.1.1 on 2018-10-21 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0002_auto_20181021_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='date',
            field=models.DateField(verbose_name='Date de parution'),
        ),
    ]
