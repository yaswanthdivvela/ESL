# Generated by Django 2.2.6 on 2019-10-22 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20191022_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='pic',
            field=models.FileField(upload_to=''),
        ),
    ]
