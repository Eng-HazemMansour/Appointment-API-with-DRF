from django.db import models


class Doctor(models.Model):
    doctor_name = models.CharField(max_length = 50)


    def __str__(self):
        return self.doctor_name


class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length = 50)
    registration_day = models.DateField("Date registered")
    registration_hour = models.TimeField("Time registered")
    waiting_status = models.BooleanField(default = True)

    def __str__(self):
        return self.patient_name

    @property
    def is_waiting(self):
        return bool(self.waiting_status)

