# Generated by Django 4.1.7 on 2023-03-25 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Duck_or_Penguin', '0002_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageAnimals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]