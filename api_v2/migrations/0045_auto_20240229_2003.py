# Generated by Django 3.2.20 on 2024-02-29 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0044_alter_spell_material_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spell',
            old_name='target_count',
            new_name='target_count_txt',
        ),
        migrations.AlterField(
            model_name='castingoption',
            name='range',
            field=models.TextField(help_text='Description of the range of the spell.', null=True),
        ),
    ]