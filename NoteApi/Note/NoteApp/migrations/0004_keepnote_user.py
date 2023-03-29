# Generated by Django 4.1.7 on 2023-03-28 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NoteApp', '0003_alter_keepnote_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='keepnote',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]