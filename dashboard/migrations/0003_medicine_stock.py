# Generated by Django 4.2 on 2024-03-26 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_report_alter_medicine_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='stock',
            field=models.CharField(default=0, max_length=55),
            preserve_default=False,
        ),
    ]
