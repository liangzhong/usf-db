# Generated by Django 2.2.7 on 2019-11-17 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eresource', '0002_auto_20191111_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='ebook',
            name='author',
        ),
        migrations.AddField(
            model_name='ebook',
            name='author',
            field=models.ManyToManyField(to='eresource.Author'),
        ),
    ]
