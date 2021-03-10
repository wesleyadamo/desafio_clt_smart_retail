from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


HOTEL_NAMES = (
    ('Lakewood', 'Lakewood'),
    ('Bridgewood', 'Bridgewood'),
    ('Ridgewood', 'Ridgewood'),

)


class Hotel(models.Model):
    name = models.CharField(max_length=30, default='Lakewood', choices=HOTEL_NAMES, unique=True)
    classification = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.name


CLIENT_TYPE = (
    ('Reward', 'Reward'),
    ('Regular', 'Regular')
)


class CustomerFee(models.Model):
    client_type = models.CharField(max_length=10, default='Regular', choices=CLIENT_TYPE)
    weekday_rate = models.FloatField(validators=[MinValueValidator(0)], null=False, blank=False)
    weekend_rate = models.FloatField(validators=[MinValueValidator(0)], null=False, blank=False)
    hotel = models.ForeignKey(Hotel, verbose_name='customer_fee', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('hotel', 'client_type'),)
