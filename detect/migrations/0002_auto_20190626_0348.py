# Generated by Django 2.2.2 on 2019-06-26 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detect', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handler',
            name='image',
            field=models.ImageField(upload_to='images/%Y/%m/%d'),
        ),
    ]