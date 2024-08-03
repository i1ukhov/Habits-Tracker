# Generated by Django 4.2.2 on 2024-08-03 08:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("habits", "0003_alter_habits_award"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habits",
            name="user",
            field=models.ForeignKey(
                blank=True,
                help_text="Habit owner",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
    ]
