from django.contrib import admin
from bookings import models
# Register your models here.

admin.site.register(models.Movie)
admin.site.register(models.Show)
admin.site.register(models.Reservation)
admin.site.register(models.Seat)
admin.site.register(models.Screen)
admin.site.register(models.Theatre)
admin.site.register(models.City)
admin.site.register(models.ReservedSeat)
