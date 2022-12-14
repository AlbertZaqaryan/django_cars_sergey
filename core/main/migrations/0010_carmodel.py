# Generated by Django 4.1 on 2022-08-30 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_callus'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media', verbose_name='CarModel image')),
                ('title', models.TextField(verbose_name='CarModel about')),
                ('price', models.CharField(max_length=30, verbose_name='CarModel price')),
            ],
            options={
                'verbose_name': 'CarModel',
                'verbose_name_plural': 'CarModels',
            },
        ),
    ]
