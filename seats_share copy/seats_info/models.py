from django.db import models

FLOOR_CHOICES = (
	(3, 3),
	(4, 4),
	(5, 5),
	(7, 7),
	(8, 8),
	(9, 9),
	(10, 10),
	)

AREA_CHOICES = (
	("A", "A"),
	("B", "B"),
	("C", "C"),
	("D", "D"),
	("E", "E"),
	)

SEAT_CHOICES = (
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(6, 6),
	)

class DefaultSeatInfo(models.Model):
	floor = models.CharField(max_length=2, choices=FLOOR_CHOICES)
	area = models.CharField(max_length=1,choices=AREA_CHOICES)
	table = models.CharField(max_length=2)
	seats = models.CharField(max_length=1)
	
class SeatInfo(models.Model):
	floor = models.CharField(max_length=2, choices=FLOOR_CHOICES)
	area = models.CharField(max_length=1,choices=AREA_CHOICES)
	table = models.CharField(max_length=2)
	seats = models.CharField(max_length=1, choices=SEAT_CHOICES)