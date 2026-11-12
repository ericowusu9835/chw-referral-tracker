from django.test import TestCase
from .models import Referral

class ReferralTest(TestCase):
    def test_create_referral(self):
        referral = Referral.objects.create(
            patient_name="Ama Mensah",
            age=34,
            community="Madina",
            phone="0551234567",
            symptoms="High fever",
            status="pending",
            is_serious=False
        )
        self.assertEqual(referral.patient_name, "Ama Mensah")
        self.assertEqual(referral.status, "pending")
        self.assertEqual(Referral.objects.count(), 1)

    def test_referral_str(self):
        referral = Referral.objects.create(
            patient_name="Kwame",
            age=25,
            community="Legon",
            symptoms="Malaria",
            status="pending",
        )
        # Your __str__ is "Kwame - Legon"
        self.assertEqual(str(referral), "Kwame - Legon")