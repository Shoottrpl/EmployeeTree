# Generated by Django 5.1.2 on 2024-10-26 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_employee_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employment',
            field=models.DateTimeField(),
        ),
    ]
