from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    date_of_hire = models.DateField()
    email = models.EmailField(unique=True)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='subordinates')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
