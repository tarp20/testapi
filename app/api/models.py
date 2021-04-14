from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid


# def validate_color(color):
#     match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color)
#     if match == False:
#         raise ValidationError(
#             _('%(color)s is not an even number'),
#             params={'color': color},
#         )


class Car(models.Model):
    '''
    Car Model
    '''

    unique_id = models.UUIDField(default=uuid.uuid4(), editable=False)
    make = models.CharField(max_length=56, blank=False, null=False)
    color = models.CharField(max_length=56, blank=False, null=False)
    production_year = models.IntegerField(blank=False, validators=[
        MaxValueValidator(2021),
        MinValueValidator(1960),
    ])
    avg_fuel_consumption_per_100km = models.DecimalField(blank=False, null=False, max_digits=5, decimal_places=2,
                                                         validators=[
                                                             MaxValueValidator(20),
                                                             MinValueValidator(2),
                                                         ])
    max_passengers = models.PositiveIntegerField(blank=False, null=False,
                                                 validators=[
                                                     MinValueValidator(1),
                                                     MaxValueValidator(10),
                                                 ])
    created_at = models.DateTimeField(auto_now_add=True)
