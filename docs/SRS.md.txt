# Software Requirements Specification (SRS)
## CHW Referral Tracker

### 1. Introduction
Community Health Workers (CHWs) in Ghana refer patients to clinics using paper forms. Papers get lost, clinics do not know a patient is coming, and follow-up is difficult. This system digitizes referrals to solve that problem.

### 2. Team
- Project Manager:
- Lead Developer: Eric Owusu
- Tester:
- Documentation Lead:

### 3. Core Features
1. Add Referral - CHW creates a referral with patient_name, age, community, phone, symptoms, status, is_serious
2. View All Referrals - List and search by community or patient name
3. Update Status - Pending -> Referred -> Completed
4. Medicine & Prescription - Record medicines and prescriptions linked to a referral
5. SMS Notification - When a referral is created, an SMS is sent to the clinic using the Arkesel API

### 4. Functional Requirements
- FR1: The system shall allow a CHW to create a referral.
- FR2: The system shall list all referrals.
- FR3: The system shall allow updating the referral status.
- FR4: The system shall send an SMS when a new referral is created.
- FR5: The system shall store data in a database (SQLite / Django ORM).

### 5. Non-Functional Requirements
- Usable on mobile and laptop
- Simple forms, no training needed
- Fast - pages load in under 2 seconds

### 6. Database Models
- Referral(patient_name, age, community, phone, symptoms, status, is_serious, created_at)
- Medicine(name, dosage, stock)
- Prescription(referral, medicine, instructions)

### 7. External Service
- Arkesel SMS API - https://sms.arkesel.com/api/v2/sms/send