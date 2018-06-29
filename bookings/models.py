from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    duration = models.IntegerField()

    def __str__(self):
        return self.name


class Theatre(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.ForeignKey(City,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Screen(models.Model):
    name = models.CharField(max_length=10)
    theatre = models.ForeignKey(Theatre,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.theatre)+' - '+str(self.name)


class Seat(models.Model):
    row = models.CharField(max_length=1)
    number = models.IntegerField()
    screen = models.ForeignKey(Screen,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.screen)+' - '+str(self.row)+str(self.number)


class Show(models.Model):
    date = models.DateField()
    time = models.TimeField()
    screen = models.ForeignKey(Screen,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.screen)+' '+str(self.date)+' '+str(self.time)


class Reservation(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id)


class ReservedSeat(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.DO_NOTHING)
    reservation = models.ForeignKey(Reservation,on_delete=models.CASCADE)
    show = models.ForeignKey(Show,on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.seat)
