# Generated by Django 5.1.1 on 2024-10-05 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_auto_20240806_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='spell_list',
            field=models.ManyToManyField(through='api.MonsterSpell', to='api.spell'),
        ),
    ]
