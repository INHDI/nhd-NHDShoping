# Generated by Django 2.2.12 on 2020-04-17 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('San_Pham', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spbanmodel',
            name='Mo_ta',
            field=models.SmallIntegerField(choices=[(1, 'Đang Sale 10 %'), (2, 'Đang giảm mạnh'), (3, 'Đang Sale 50 %')], verbose_name='Mô Tả'),
        ),
    ]
