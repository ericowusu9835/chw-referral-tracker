from django.db import models

class Referral(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('referred', 'Referred'),
        ('completed', 'Completed'),
    ]
    patient_name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    community = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    symptoms = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    is_serious = models.BooleanField(default=False, help_text="Tick if this is a serious / urgent referral")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.patient_name} - {self.community}"

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100, help_text="e.g. 500mg, 2 times a day")
    stock = models.IntegerField(default=0, help_text="How many left in stock")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} - {self.dosage} (Stock: {self.stock})"

class Prescription(models.Model):
    referral = models.ForeignKey(Referral, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    prescribed_by = models.CharField(max_length=100, help_text="Name of Nurse / Prescriber")
    prescriber_photo = models.ImageField(upload_to='prescriber_photos/', blank=True, null=True, help_text="Snap face photo for verification before prescribing")
    is_verified = models.BooleanField(default=False, help_text="Tick only after face/photo is verified")
    quantity = models.IntegerField(default=1)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.medicine.name} for {self.referral.patient_name}"