# Generated by Django 3.2.3 on 2021-05-26 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
    ]
