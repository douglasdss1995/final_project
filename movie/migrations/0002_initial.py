# Generated by Django 4.0.3 on 2022-04-10 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie', '0001_initial_schema'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(db_column='name', max_length=128, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': '"movie"."category"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(db_column='title', max_length=256, verbose_name='Title')),
                ('category', models.ForeignKey(db_column='id_category', on_delete=django.db.models.deletion.DO_NOTHING, related_name='category_in_app_%(app_label)s_table_table_%(class)s', to='movie.category')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
                'db_table': '"movie"."movie"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(db_column='name', max_length=125, verbose_name='Name')),
                ('email', models.EmailField(db_column='email', max_length=254, unique=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Subscriber',
                'verbose_name_plural': 'Subscribers',
                'db_table': '"movie"."subscriber"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SubscriberMovie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('movie', models.ForeignKey(db_column='id_movie', on_delete=django.db.models.deletion.DO_NOTHING, related_name='movies_in_app_%(app_label)s_table_table_%(class)s', to='movie.movie')),
                ('subscriber', models.ForeignKey(db_column='id_subscriber', on_delete=django.db.models.deletion.DO_NOTHING, related_name='subscribers_in_app_%(app_label)s_table_table_%(class)s', to='movie.subscriber')),
            ],
            options={
                'verbose_name': 'Subscriber movie',
                'verbose_name_plural': 'Subscriber movies',
                'db_table': '"movie"."subscriber_movie"',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('release_date', models.DateField(db_column='release_date', verbose_name='Release date')),
                ('movie', models.ForeignKey(db_column='id_movie', on_delete=django.db.models.deletion.DO_NOTHING, related_name='movies_in_app_%(app_label)s_table_table_%(class)s', to='movie.movie')),
            ],
            options={
                'verbose_name': 'Announcement',
                'verbose_name_plural': 'Announcements',
                'db_table': '"movie"."announcement"',
                'managed': True,
            },
        ),
        migrations.AddIndex(
            model_name='subscribermovie',
            index=models.Index(fields=['subscriber'], name='subscriber__id_subs_4e4e13_idx'),
        ),
        migrations.AddIndex(
            model_name='subscribermovie',
            index=models.Index(fields=['movie'], name='subscriber__id_movi_034580_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='subscribermovie',
            unique_together={('subscriber', 'movie')},
        ),
    ]