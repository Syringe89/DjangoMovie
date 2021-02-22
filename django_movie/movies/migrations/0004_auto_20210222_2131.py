# Generated by Django 3.1.6 on 2021-02-22 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20210222_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieshots',
            name='description',
            field=models.TextField(blank=True, default=0, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movieshots',
            name='title',
            field=models.CharField(blank=True, default=0, max_length=100, verbose_name='Заголовок'),
            preserve_default=False,
        ),
    ]
