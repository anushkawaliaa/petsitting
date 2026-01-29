from django.db import models

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('contacted', 'Contacted'),
        ('paid', 'Paid'),
        ('completed', 'Completed'),
    ]

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    pet_type = models.CharField(max_length=50)
    number_of_pets = models.PositiveIntegerField()
    duration = models.CharField(max_length=50)
    address = models.TextField()
    special_instructions = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

