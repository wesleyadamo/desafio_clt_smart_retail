from django.contrib import admin

# Register your models here.
from hotel.models import CustomerFee, Hotel

admin.site.register(CustomerFee)
admin.site.register(Hotel)
