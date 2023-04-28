# Generated by Django 4.1 on 2022-11-12 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholar', '0007_delete_paperreferences_delete_papers'),
    ]

    operations = [
        migrations.CreateModel(
            name='ByAuthorPaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('by_author', models.TextField()),
                ('paper_id', models.TextField()),
            ],
        ),
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
                ('url', models.TextField(null=True)),
                ('volume', models.TextField(null=True)),
                ('fos', models.TextField(null=True)),
                ('issue', models.TextField(null=True)),
                ('year', models.IntegerField(null=True)),
                ('authors', models.TextField(null=True)),
                ('lang', models.TextField(null=True)),
                ('doc_type', models.TextField(null=True)),
                ('page_end', models.TextField(null=True)),
                ('publisher', models.TextField(null=True)),
                ('n_citation', models.IntegerField(null=True)),
                ('abstract', models.TextField(null=True)),
                ('venue', models.TextField(null=True)),
                ('page_start', models.TextField(null=True)),
                ('doi', models.TextField(null=True)),
                ('title', models.TextField(null=True)),
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('keyword', models.TextField(null=True)),
            ],
        ),
    ]
