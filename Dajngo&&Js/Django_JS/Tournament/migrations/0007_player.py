# Generated by Django 5.0.6 on 2024-07-26 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tournament', '0006_alter_tournament_num_players'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
