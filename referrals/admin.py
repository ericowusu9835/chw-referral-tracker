from django.contrib import admin
from .models import Referral

@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'is_serious', 'status', 'created_at')
    list_filter = ('is_serious', 'status')
    search_fields = ('patient_name', 'community')

    actions = ['mark_as_serious', 'mark_as_normal']

    @admin.action(description="Mark as SERIOUS referral")
    def mark_as_serious(self, request, queryset):
        queryset.update(is_serious=True)

    @admin.action(description="Mark as Normal referral")
    def mark_as_normal(self, request, queryset):
        queryset.update(is_serious=False)