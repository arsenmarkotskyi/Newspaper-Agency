# Generated by Django 5.1.2 on 2024-10-29 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redactor',
            name='years_of_experience',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]