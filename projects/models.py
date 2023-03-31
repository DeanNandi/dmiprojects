from django.db import models


class Projects(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    date_of_creation = models.CharField(max_length=255)


class Inkind(models.Model):
    item_name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    program_name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    date_supplied = models.CharField(max_length=255)


class Cash(models.Model):
    amount_received = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    program_name = models.CharField(max_length=255)
    date_issued = models.CharField(max_length=255)


class Purchases(models.Model):
    item_bought = models.CharField(max_length=255)
    item_price = models.CharField(max_length=255)
    program_name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    date_bought = models.CharField(max_length=255)


class Brought(models.Model):
    item_brought = models.CharField(max_length=255)
    item_brand = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    program_name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    date_brought = models.CharField(max_length=255)


class Dispensing(models.Model):
    item_name = models.CharField(max_length=255)
    item_brand = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    program_name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    date_dispensed = models.CharField(max_length=255)
