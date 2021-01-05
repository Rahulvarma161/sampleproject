# Generated by Django 3.1.5 on 2021-01-05 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0002_auto_20210105_0534'),
    ]

    operations = [
        migrations.CreateModel(
            name='savecategorys',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('categories_id', models.IntegerField(blank=True, null=True)),
                ('subcategory_id', models.IntegerField(blank=True, null=True)),
                ('isactive', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'table_savecategorys',
            },
        ),
        migrations.DeleteModel(
            name='savecategory',
        ),
    ]
