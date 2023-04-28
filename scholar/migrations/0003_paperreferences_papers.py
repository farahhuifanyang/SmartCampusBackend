# Generated by Django 4.1 on 2022-11-12 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholar', '0002_teacherstudents'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaperReferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citing', models.TextField()),
                ('cited', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Papers',
            fields=[
                ('n_citation', models.IntegerField()),
                ('year', models.IntegerField()),
                ('url', models.TextField()),
                ('volume', models.TextField()),
                ('fos', models.TextField()),
                ('issue', models.TextField()),
                ('authors', models.TextField()),
                ('lang', models.TextField()),
                ('doc_type', models.TextField()),
                ('page_end', models.TextField()),
                ('publisher', models.TextField()),
                ('abstract', models.TextField()),
                ('venue', models.TextField()),
                ('page_start', models.TextField()),
                ('doi', models.TextField()),
                ('title', models.TextField()),
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('keyword', models.TextField()),
            ],
        ),
    ]