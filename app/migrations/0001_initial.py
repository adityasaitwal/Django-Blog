# Generated by Django 3.1.7 on 2021-05-17 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('date', models.DateField()),
                ('img_1', models.ImageField(upload_to='')),
            ],
        ),
    ]
