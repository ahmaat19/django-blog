# Generated by Django 3.1 on 2020-11-09 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
                ('content', models.TextField()),
                ('published', models.BooleanField(default=False)),
                ('tags', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.category')),
            ],
        ),
    ]