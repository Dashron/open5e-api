# Generated by Django 3.2.20 on 2024-03-29 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0037_alter_monster_legendary_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='bonus_actions_json',
            field=models.TextField(default=None, null=True),
        ),
    ]