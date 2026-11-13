from django.contrib import admin
from .models import Referral

@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ('referral_code', 'patient_name', 'community', 'age', 'is_serious', 'status', 'follow_up_done', 'created_at')
    list_filter = ('status', 'is_serious', 'follow_up_done', 'community')
    search_fields = ('patient_name', 'phone', 'community', 'referral_code', 'symptoms')
    list_editable = ('status', 'follow_up_done')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('👤 Patient Info', {
            'fields': ('patient_name', 'phone', 'age', 'community')
        }),
        ('🤒 Medical Info', {
            'fields': ('symptoms', 'prescription', 'is_serious')
        }),
        ('🏥 Referral Info', {
            'fields': ('referral_code', 'status', 'feedback', 'follow_up_done', 'created_at')
        }),
    )