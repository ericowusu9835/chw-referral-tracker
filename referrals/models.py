from django.db import models

class Referral(models.Model):
    STATUS_CHOICES = [
        ('Referred', 'Referred'),
        ('Completed', 'Completed'),
        ('Rejected', 'Rejected'),
    ]

    patient_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    community = models.CharField(max_length=100)
    symptoms = models.TextField()
    prescription = models.TextField(blank=True, null=True)
    is_serious = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Referred')
    referral_code = models.CharField(max_length=20, blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    follow_up_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} - {self.community} - {self.status}"