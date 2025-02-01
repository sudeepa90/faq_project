# Generated by Django 5.1.5 on 2025-02-01 05:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', ckeditor.fields.RichTextField()),
                ('question_hi', models.TextField(blank=True)),
                ('answer_hi', ckeditor.fields.RichTextField(blank=True)),
                ('question_bn', models.TextField(blank=True)),
                ('answer_bn', ckeditor.fields.RichTextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
