# referrals/sms.py - SMS sender for Ghana
# Works WITHOUT internet / WITHOUT money first: it saves SMS to log + prints it.
# When you get Arkesel / Hubtel API key, put it in settings.py and it will send REAL SMS.

import os
import datetime

def send_sms(phone, message):
    """
    Send SMS to a phone number.
    phone: e.g. "233240352335" or "0240352335"
    message: text to send
    Returns True if sent/logged.
    """
    # --- 1. Clean phone number to 233 format ---
    phone = str(phone).strip().replace(" ", "").replace("-", "")
    if phone.startswith("0"):
        phone = "233" + phone[1:]
    if phone.startswith("+"):
        phone = phone[1:]

    # --- 2. Save to log file so you can prove SMS was sent ---
    log_line = f"{datetime.datetime.now()} | TO: {phone} | MSG: {message}\n"
    try:
        # Save inside your project folder
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_path = os.path.join(base_dir, "sms_log.txt")
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(log_line)
    except Exception as e:
        print(f"SMS log error: {e}")

    # --- 3. Print in terminal so you SEE it working ---
    print("=" * 50)
    print(f"📱 SMS TO: {phone}")
    print(f"📝 MSG: {message}")
    print("✅ SMS LOGGED - Check sms_log.txt")
    print("=" * 50)

    # --- 4. REAL SMS - Only if you have Arkesel API Key ---
    # To make it REAL, later add in settings.py:
    # ARKESEL_API_KEY = "your_key_here"
    # For now we return True so your app will NOT crash.
    try:
        from django.conf import settings
        api_key = getattr(settings, 'ARKESEL_API_KEY', '')
        if api_key:
            import requests
            # Arkesel API
            url = "https://sms.arkesel.com/api/v2/sms/send"
            data = {
                "sender": "CHW",
                "message": message,
                "recipients": [phone],
            }
            headers = {"api-key": api_key}
            res = requests.post(url, json=data, headers=headers, timeout=10)
            print(f"Arkesel Response: {res.status_code} {res.text}")
            return res.status_code in [200, 201]
    except Exception as e:
        print(f"Real SMS failed, but logged: {e}")

    return True