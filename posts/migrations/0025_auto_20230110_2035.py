# Generated by Django 2.2.16 on 2023-01-10 20:35

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0024_auto_20230109_1545'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='self_follow',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, user=django.db.models.expressions.F('author')), name='self_follow'),
        ),
    ]
