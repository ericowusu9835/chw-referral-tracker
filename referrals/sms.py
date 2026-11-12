# referrals/sms.py - SEND TO ANY NUMBER VERSION
# Just put your key once, then you can send to anybody.

import requests

# ============ CHANGE HERE ONLY ============
API_KEY = "bmxvT3FXTGJ6amRidU91T01GanI"
SENDER_ID = "Arkesel"
# ===========================================

def format_number(phone):
    phone = str(phone).strip().replace(" ", "").replace("-", "").replace("+", "")
    if phone.startswith("0"):
        phone = "233" + phone[1:]
    return phone

def send_sms(to_number, message):
    """Send to ANY number. Example: send_sms("0241234567", "Hello")"""
    if not API_KEY or API_KEY == "PASTE_YOUR_ARKESEL_KEY_HERE":
        print("ERROR: Put your Arkesel API Key for sms.py first")
        return False

    to_number = format_number(to_number)

    url = "https://sms.arkesel.com/api/v2/sms/send"
    payload = {
        "action": "send-sms",
        "api_key": API_KEY,
        "to": to_number,
        "from": SENDER_ID,
        "sms": message
    }

    try:
        response = requests.post(url, json=payload, timeout=20)
        print("Arkesel response:", response.text)
        data = response.json()
        if str(data.get("code")) == "1000":
            print(f"SMS SENT to {to_number} SUCCESSFULLY")
            return True
        else:
            print("SMS FAILED - Check key, sender ID or balance")
            return False
    except Exception as e:
        print("SMS Failed:", e)
        return False

# ===== SEND TO ANY NUMBER BY TYPING =====
# Run: python referrals/sms.py
# E go ask you: Enter phone number, Enter message
if __name__ == "__main__":
    print("=== SEND SMS TO ANY NUMBER ===")
    print("Example number: 0240352335 or 233240352335")
    print("")

    phone = input("Enter phone number: ")
    msg = input("Enter message: ")

    if phone.strip() == "" or msg.strip() == "":
        print("You must enter number and message!")
    else:
        send_sms(phone, msg)