# Generated by Django 3.2.6 on 2021-08-24 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='agentname',
            fields=[
                ('name_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('pollingunit_uniqueid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='announced_lga_results',
            fields=[
                ('result_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('lga_name', models.CharField(max_length=200)),
                ('party_abbreviation', models.CharField(max_length=50)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=200)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='announced_pu_results',
            fields=[
                ('result_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('polling_unit_uniqueid', models.CharField(max_length=200)),
                ('party_abbreviation', models.CharField(max_length=50)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=7)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='announced_state_results',
            fields=[
                ('result_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=200)),
                ('party_abbreviation', models.CharField(max_length=50)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=200)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='announced_ward_results',
            fields=[
                ('result_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('ward_name', models.CharField(max_length=200)),
                ('party_abbreviation', models.CharField(max_length=50)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=200)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='lga',
            fields=[
                ('uniqueid', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('lga_id', models.IntegerField()),
                ('lga_name', models.CharField(max_length=200)),
                ('state_id', models.IntegerField()),
                ('lga_description', models.TextField()),
                ('entered_by_user', models.CharField(max_length=200)),
                ('date_entered', models.DateTimeField(max_length=200)),
                ('user_ip_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='party',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('partyid', models.CharField(max_length=200)),
                ('partyname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='polling_unit',
            fields=[
                ('uniqueid', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('polling_unit_id', models.IntegerField()),
                ('ward_id', models.IntegerField()),
                ('lga_id', models.IntegerField()),
                ('uniquewardid', models.IntegerField()),
                ('polling_unit_number', models.CharField(max_length=200)),
                ('polling_unit_name', models.CharField(max_length=200)),
                ('polling_unit_description', models.TextField()),
                ('lat', models.CharField(max_length=50)),
                ('long', models.CharField(max_length=200)),
                ('entered_by_user', models.CharField(max_length=200)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='states',
            fields=[
                ('state_id', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('state_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ward',
            fields=[
                ('uniqueid', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('ward_id', models.IntegerField()),
                ('ward_name', models.CharField(max_length=50)),
                ('lga_id', models.IntegerField()),
                ('ward_description', models.TextField()),
                ('entered_by_user', models.CharField(max_length=200)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
        ),
    ]