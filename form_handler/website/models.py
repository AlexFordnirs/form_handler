from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    birth = models.DateTimeField(null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    group = models.CharField(max_length=30, default=None, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated = models.DateTimeField(auto_created=True, auto_now=True)

    class Meta:
        verbose_name_plural = 'Students'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



