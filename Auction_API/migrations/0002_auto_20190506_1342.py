# Generated by Django 2.2.1 on 2019-05-06 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auction_API', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auction',
            options={'ordering': ('start_datetime',)},
        ),
    ]
