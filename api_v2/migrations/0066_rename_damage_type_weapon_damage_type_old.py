# Generated by Django 3.2.20 on 2024-03-15 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0065_remove_creatureattack_extra_damage_type_old'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weapon',
            old_name='damage_type',
            new_name='damage_type_old',
        ),
    ]