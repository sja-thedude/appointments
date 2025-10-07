from django.db import models

class Appointment(models.Model):
    provider_name = models.CharField(max_length=100)
    appointment_time = models.DateTimeField()
    client_email = models.EmailField()

    def __str__(self):
        return f"{self.provider_name} - {self.appointment_time}"
