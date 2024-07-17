# Generated by Django 5.0.3 on 2024-05-30 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text: ')),
                ('title', models.CharField(max_length=50, verbose_name='Title: ')),
                ('address', models.CharField(max_length=50, verbose_name='Adress: ')),
                ('info', models.CharField(max_length=50, verbose_name='Info: ')),
                ('number', models.CharField(max_length=50, verbose_name='Number: ')),
            ],
        ),
    ]