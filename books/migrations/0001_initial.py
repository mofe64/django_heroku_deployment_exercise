# Generated by Django 3.2.3 on 2021-05-16 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, unique=True)),
                ('author', models.CharField(max_length=30)),
                ('pages', models.IntegerField(default=0)),
                ('coverImage', models.ImageField(upload_to='book_covers')),
                ('date_listed', models.DateField(auto_now_add=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('book_file', models.FileField(upload_to='book_files')),
            ],
        ),
    ]
