# Generated by Django 3.2.6 on 2021-08-25 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announced_pu_results',
            name='result_id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]