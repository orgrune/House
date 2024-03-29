from django.db import models

#House Model
class House(models.Model):
    area_unit = models.CharField(max_length=100, blank=True, null=True)
    bathrooms = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    bedrooms = models.IntegerField(blank=True, null=True)
    home_size = models.IntegerField(blank=True, null=True)
    home_type = models.CharField(max_length=100, blank=True, null=True)
    last_sold_date = models.DateField(blank=True, null=True)
    last_sold_price = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    property_size = models.IntegerField(blank=True, null=True)
    rent_price = models.IntegerField(blank=True, null=True)
    rentzestimate_amount = models.IntegerField(blank=True, null=True)
    rentzestimate_last_updated = models.DateField(blank=True, null=True)
    tax_value = models.IntegerField(blank=True, null=True)
    tax_year = models.IntegerField(blank=True, null=True)
    year_built = models.IntegerField(blank=True, null=True)
    zestimate_amount = models.IntegerField(blank=True, null=True)
    zestimate_last_updated =  models.DateField(blank=True, null=True)
    zillow_id = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.IntegerField(blank=True, null=True)