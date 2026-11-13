# Risk Register - CHW Referral Tracker

| ID | Risk | Likelihood | Impact | Mitigation / What We Did |
| --- | --- | --- | --- | --- |
| R1 | Team member unavailable / sick | Medium | High | Roles rotate every 3 weeks, code on GitHub so anyone can continue, tasks shared in group chat |
| R2 | No internet / power cut during demo | Medium | High | Demo video recorded as backup, SQLite works offline, laptop fully charged + hotspot |
| R3 | Patient data / phone numbers leaked | Low | High | No real patient data used - test data only, Admin requires login, CSRF token on forms |
| R4 | SMS Sandbox (Arkesel) fails / no credit | Medium | Medium | WhatsApp link as fallback external service, SMS logged in Admin even if sandbox down |
| R5 | Wrong status counts (lowercase vs uppercase) | High | Medium | Fixed with `status__iexact` filter, added automated test for status |
| R6 | Git merge conflict / one member overwrites code | Medium | High | Each member works on separate branch / separate docs file, pull before push |
| R7 | Scope too big, not finished by Week 8 | Medium | High | Limited to 5 core features only, froze features in Sprint 3, focused on docs + demo |
| R8 | Laptop / DB lost | Low | High | Weekly push to GitHub, db.sqlite3 backed up, README with setup steps |

**Top 3 Risks for Demo:** R2 (Demo internet), R4 (SMS), R6 (Git conflict)
**Owner:** Project Manager reviews this every Sprint.
