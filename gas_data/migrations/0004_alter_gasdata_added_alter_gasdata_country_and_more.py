# Generated by Django 4.2.7 on 2023-11-11 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas_data', '0003_rename_dashboard_gasdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasdata',
            name='added',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='gasdata',
            name='country',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='gasdata',
            name='end_year',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='gasdata',
            name='impact',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='gasdata',
            name='insight',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='gasdata',
            name='pestle',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='gasdata',
            name='published',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='gasdata',
            name='region',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='gasdata',
            name='sector',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='gasdata',
            name='source',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='gasdata',
            name='start_year',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='gasdata',
            name='title',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='gasdata',
            name='topic',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='gasdata',
            name='url',
            field=models.CharField(max_length=512),
        ),
    ]
