# Generated by Django 3.1.7 on 2021-03-28 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reports.report'),
        ),
    ]
