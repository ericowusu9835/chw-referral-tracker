# UML Design - CHW Referral Tracker

## Use Case Diagram
Actor: Community Health Worker (CHW)
- CHW -> Add Referral
- CHW -> View Referrals
- CHW -> Update Status
- CHW -> Add Medicine
- System -> Send SMS to Clinic
- Send whatspp messages to nurse

## Class Diagram
Referral
- patient_name: string
- age: int
- community: string
- phone: string
- symptoms: text
- status: string
- is_serious: boolean
- created_at: datetime

Medicine
- name: string
- dosage: string
- stock: int

Prescription
- referral: Referral
- medicine: Medicine
- instructions: text

## Sequence - New Referral
1. CHW fills referral form
2. System saves Referral to database
3. System calls Arkesel SMS API
4. Clinic receives SMS
5. System shows success page
6. nurses receives WhatsApp messages
