# Generated by Django 3.0.6 on 2020-08-18 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='post upload images')),
                ('category', models.CharField(choices=[('politics', 'Politics'), ('education', 'Education'), ('foods', 'Foods'), ('relationship', 'Relationship'), ('gossip', 'Gossip'), ('counselling', 'Counselling'), ('religion', 'Religion'), ('sports', 'Sports'), ('technology', 'Technology'), ('fashion', 'Fashion')], max_length=20)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Blog Posts',
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Comments',
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Favorites',
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Likes',
                'ordering': ['-time'],
            },
        ),
    ]
