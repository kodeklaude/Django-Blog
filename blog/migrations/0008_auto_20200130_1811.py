# Generated by Django 2.2.3 on 2020-01-30 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_created_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
    ]
