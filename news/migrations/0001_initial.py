# Generated by Django 4.2.4 on 2023-08-15 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating', models.SmallIntegerField(default=0)),
                ('UserName', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameCategory', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Choise', models.CharField(choices=[('nw', 'новость'), ('ar', 'статья')], default='nw', max_length=2)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=64)),
                ('text_content', models.TextField()),
                ('rating_content', models.SmallIntegerField(default=0)),
                ('Turn_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.author')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relations_OnCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category')),
                ('relations_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='relations_category',
            field=models.ManyToManyField(through='news.PostCategory', to='news.category'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_comment', models.TextField()),
                ('date_comment', models.DateTimeField(auto_now_add=True)),
                ('rating_comment', models.SmallIntegerField(default=0)),
                ('relationsPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post')),
                ('relationsUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
