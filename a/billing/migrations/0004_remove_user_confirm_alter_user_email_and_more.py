# Generated by Django 4.2.3 on 2023-07-17 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_alter_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='confirm',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='kzykizdaet@example.com', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='passwd',
            field=models.CharField(default='mbOVSB80', max_length=100),
        ),
    ]
