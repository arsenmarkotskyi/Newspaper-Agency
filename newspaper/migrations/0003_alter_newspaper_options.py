# Generated by Django 5.1.2 on 2024-11-10 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0002_alter_redactor_years_of_experience'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newspaper',
            options={'ordering': ['-published_date']},
        ),
    ]