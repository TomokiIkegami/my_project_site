# Generated by Django 5.0.1 on 2024-01-21 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj_overview', '0002_articleinfo_article2_articleinfo_img1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleinfo',
            name='img1',
        ),
        migrations.AddField(
            model_name='articleinfo',
            name='img_path_1',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
