# Generated by Django 5.0.6 on 2024-07-22 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_rename_id_member_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
