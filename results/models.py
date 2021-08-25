from django.db import models


class agentname(models.Model):
    name_id = models.IntegerField(primary_key=True, editable=False)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    pollingunit_uniqueid = models.IntegerField()


class announced_lga_results(models.Model):
    result_id = models.IntegerField(primary_key=True,  editable=False)
    lga_name = models.CharField(max_length=200)
    party_abbreviation = models.CharField(max_length=50)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=200)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=200)


class announced_pu_results(models.Model):
    result_id = models.AutoField(primary_key=True, editable=False)
    polling_unit_uniqueid = models.CharField(max_length=200)
    party_abbreviation = models.CharField(max_length=50)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=7)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=100)


class announced_state_results(models.Model):
    result_id = models.IntegerField(primary_key=True, editable=False)
    state_name = models.CharField(max_length=200)
    party_abbreviation = models.CharField(max_length=50)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=200)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=100)


class announced_ward_results(models.Model):
    result_id = models.IntegerField(primary_key=True, editable=False)
    ward_name = models.CharField(max_length=200)
    party_abbreviation = models.CharField(max_length=50)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=200)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=100)


class lga(models.Model):
    uniqueid = models.IntegerField(primary_key=True, editable=False)
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=200)
    state_id = models.IntegerField()
    lga_description = models.TextField()
    entered_by_user = models.CharField(max_length=200)
    date_entered = models.DateTimeField(max_length=200)
    user_ip_address = models.CharField(max_length=200)

class party(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    partyid = models.CharField(max_length=200)
    partyname = models.CharField(max_length=50)

class polling_unit(models.Model):
    uniqueid = models.IntegerField(primary_key=True, editable=False)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    uniquewardid = models.IntegerField()
    polling_unit_number = models.CharField(max_length=200)
    polling_unit_name = models.CharField(max_length=200)
    polling_unit_description = models.TextField()
    lat = models.CharField(max_length=50)
    long = models.CharField(max_length=200)
    entered_by_user = models.CharField(max_length=200)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=200)


class states(models.Model):
    state_id = models.IntegerField(unique=True, primary_key=True, editable=False)
    state_name = models.CharField(max_length=200)


class ward(models.Model):
    uniqueid = models.IntegerField(unique=True, primary_key=True, editable=False)
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=50)
    lga_id = models.IntegerField()
    ward_description = models.TextField()
    entered_by_user = models.CharField(max_length=200)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

