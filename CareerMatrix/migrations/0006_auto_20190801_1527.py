# Generated by Django 2.1.11 on 2019-08-01 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CareerMatrix', '0005_detail_content21'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='content10',
            new_name='header1',
        ),
        migrations.RenameField(
            model_name='detail',
            old_name='content11',
            new_name='header2',
        ),
        migrations.RenameField(
            model_name='detail',
            old_name='content12',
            new_name='header3',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='content13',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='content14',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='content15',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='content16',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='content17',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='content18',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='content19',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='content20',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='content21',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='content4',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='content5',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='content6',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='content7',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='content8',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='content9',
        ),
        migrations.AlterField(
            model_name='detail',
            name='content1',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='detail',
            name='content2',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='detail',
            name='content3',
            field=models.TextField(blank=True, default=''),
        ),
    ]
