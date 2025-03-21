# Generated by Django 5.1 on 2025-03-11 13:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('publication_date', models.DateTimeField(verbose_name='publication date')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0)),
                ('text', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls_app.question')),
            ],
        ),
    ]
