# Generated by Django 5.2 on 2025-04-07 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_user_member_since'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='anime_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
