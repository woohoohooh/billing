# Generated by Django 4.2.3 on 2023-07-20 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0008_user_groups_user_is_superuser_user_user_permissions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
