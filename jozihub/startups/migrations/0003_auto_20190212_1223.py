# Generated by Django 2.1.7 on 2019-02-12 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0002_auto_20190212_1219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='startup',
            old_name='rel_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='startup',
            old_name='logo',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='startup',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='startup',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]