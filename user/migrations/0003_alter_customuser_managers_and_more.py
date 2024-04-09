# Generated by Django 4.2 on 2024-04-09 11:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_alter_customuser_managers_customuser_date_joined_and_more"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customuser",
            managers=[],
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="date_joined",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="email",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="is_admin",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="is_staff",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="last_name",
        ),
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterModelTable(
            name="customuser",
            table=None,
        ),
    ]
