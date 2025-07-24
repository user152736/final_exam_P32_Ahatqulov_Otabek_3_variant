from django.db import models
from django.conf import settings


class SpendingesModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(
        choices=[("food", "Oziq-ovqat"), ("transport", "Transport"), ("bills", "To‘lovlar"), ("other", "Boshqa")],
        default='other')

    def __str__(self):
        return self.title