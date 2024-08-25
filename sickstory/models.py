from django.db import models


class Patients(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name, self.last_name

class Sickness(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    start_date = models.DateField("start_date")
    end_date = models.DateField("end_date", null=True, blank=True)
    symptoms = models.CharField(max_length=200)

    def __str__(self):
        return self.name, self.symptoms