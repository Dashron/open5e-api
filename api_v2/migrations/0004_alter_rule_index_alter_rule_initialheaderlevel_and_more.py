# Generated by Django 5.1.1 on 2024-10-08 21:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0003_rename_rulegroup_ruleset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='index',
            field=models.IntegerField(default=1, help_text="A rule's position in the list of rules of the parent RuleSet"),
        ),
        migrations.AlterField(
            model_name='rule',
            name='initialHeaderLevel',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1, help_text='The header level to set rule title to'),
        ),
        migrations.AlterField(
            model_name='rule',
            name='ruleset',
            field=models.ForeignKey(help_text='The RuleSet which this Rule belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='rules', to='api_v2.ruleset'),
        ),
    ]