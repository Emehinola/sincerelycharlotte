# Generated by Django 3.0.6 on 2020-08-24 02:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0010_auto_20200821_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyThought',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thought', models.CharField(max_length=400)),
                ('time', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Daily Thoughts',
                'ordering': ['-time'],
            },
        ),
    ]
