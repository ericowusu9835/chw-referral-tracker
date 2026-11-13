from django.contrib import admin
from .models import Referral
from .sms import send_sms

@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'is_serious', 'status', 'created_at')
    list_filter = ('is_serious', 'status')
    search_fields = ('patient_name', 'community')

    actions = ['mark_as_serious', 'mark_as_normal', 'send_sms_action']

    @admin.action(description="Mark as SERIOUS referral")
    def mark_as_serious(self, request, queryset):
        queryset.update(is_serious=True)

    @admin.action(description="Mark as Normal referral")
    def mark_as_normal(self, request, queryset):
        queryset.update(is_serious=False)

    @admin.action(description="Send SMS to Clinic")
    def send_sms_action(self, request, queryset):
        count = 0
        for referral in queryset:
            message = f"New Referral: {referral.patient_name} from {referral.community}. Symptoms: {referral.symptoms}. Phone: {referral.phone}"
            # Change this to your clinic number
            clinic_number = "233XXXXXXXXX"
            if send_sms(clinic_number, message):
                count += 1
        self.message_user(request, f"SMS sent for {count} referral(s).")