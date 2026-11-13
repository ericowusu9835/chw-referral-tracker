# Individual Reflection - One Page
**Name:** [GROUP ]
**Role:** [PM / Lead Dev / Tester / Docs Lead - include rotation]
**Project:** CHW Referral Tracker

## 1. What I Did
[Write 3-4 lines: e.g. I built the tracker.html dashboard, fixed the status__iexact bug, wrote the Test Plan.]

## 2. Link to Unit 1: Database / Data Management
Our Referral model in Django is our database table. I learned how a model field becomes a column - e.g. patient_name, community, status, is_serious. I learned filtering: `Referral.objects.filter(status__iexact='Completed')` and why lowercase vs uppercase broke our counts. I also learned exporting to CSV/Excel is just reading rows from the DB.

## 3. Link to Unit 2: Software Engineering / Systems Analysis & Design
We followed the full lifecycle: SRS -> UML (Use Case, Class, Sequence) -> Sprints -> Testing -> Demo. Rotating roles every 3 weeks taught me PM vs Tester vs Dev are different skills. Our Sprint Plan and Risk Register helped us when the SMS sandbox failed - we had WhatsApp as fallback. Testing taught me automated tests catch bugs manual testing misses.

## 4. What Was Hard & What I Learned
[Write 3-4 lines: e.g. Hardest was Git merge conflict / status bug. I learned to pull before push, test after every change, and not leave docs to last week.]

## 5. If I Did It Again
[Write 2 lines: e.g. I would add Login earlier, and start docs in Sprint 1 not Sprint 4.]

**Word count:** Aim for 300-400 words, 1 page.
**Each member:** Copy this file, rename to `REFLECTION_[YOUR_NAME].md`, fill it, commit with YOUR GitHub account.
