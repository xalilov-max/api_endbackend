# Generated by Django 4.2.16 on 2024-12-04 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_comment_options_alter_course_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='liked',
            field=models.CharField(choices=[('like', 'Like'), ('dislike', 'Dislike')], max_length=10),
        ),
    ]
