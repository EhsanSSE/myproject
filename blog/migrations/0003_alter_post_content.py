# Generated by Django 4.2.17 on 2025-01-24 17:26

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=tinymce.models.HTMLField(),
        ),
    ]
