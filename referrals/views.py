from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count
from django.http import HttpResponse
from django.contrib import messages
import csv
from .models import Referral
from .sms import send_sms

def home(request):
    referrals = Referral.objects.all().order_by('-id')
    return render(request, 'referrals/home.html', {'referrals': referrals})

def tracker_view(request):
    # --- MARK AS COMPLETED ---
    if request.GET.get('complete'):
        r_id = request.GET.get('complete')
        r = get_object_or_404(Referral, id=r_id)
        r.status = 'Completed'
        r.follow_up_done = True
        r.save()
        return redirect('/tracker/?done=1')

    # --- EXPORT CSV ---
    if request.GET.get('export') == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="referrals.csv"'
        writer = csv.writer(response)
        writer.writerow(['Code', 'Patient', 'Community', 'Phone', 'Age', 'Symptoms', 'Status', 'Serious', 'Feedback', 'Date'])
        for r in Referral.objects.all().order_by('-id'):
            writer.writerow([r.referral_code, r.patient_name, r.community, r.phone, r.age, r.symptoms, r.status, 'Yes' if r.is_serious else 'No', r.feedback, r.created_at])
        return response

    # --- ADD REFERRAL FORM ---
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name', '').strip()
        community = request.POST.get('community', '').strip()
        phone = request.POST.get('phone', '').strip()
        age = request.POST.get('age', '') or 0
        symptoms = request.POST.get('symptoms', '').strip()
        is_serious = request.POST.get('is_serious') == 'on'
        if patient_name and community:
            try:
                age = int(age)
            except:
                age = 0
            r = Referral.objects.create(
                patient_name=patient_name,
                community=community,
                phone=phone,
                age=age,
                symptoms=symptoms,
                is_serious=is_serious,
                status='Referred',
            )
            r.referral_code = f"GH-{r.id:03d}"
            r.save()
            return redirect('/tracker/?added=1')

    query = request.GET.get('q', '')
    status_filter = request.GET.get('status', 'all')
    referrals = Referral.objects.all().order_by('-id')

    if query:
        referrals = referrals.filter(
            Q(patient_name__icontains=query) |
            Q(community__icontains=query) |
            Q(referral_code__icontains=query) |
            Q(phone__icontains=query) |
            Q(symptoms__icontains=query)
        )

    if status_filter == 'Completed':
        referrals = referrals.filter(status__iexact='Completed')
    elif status_filter == 'Referred':
        referrals = referrals.filter(status='Referred')
    elif status_filter == 'Rejected':
        referrals = referrals.filter(status='Rejected')
    elif status_filter == 'Serious':
        referrals = referrals.filter(is_serious=True)

    for r in referrals:
        if not r.referral_code:
            r.referral_code = f"GH-{r.id:03d}"
            r.save()

    total = Referral.objects.count()
    completed = Referral.objects.filter(status='Completed').count()
    referred = Referral.objects.filter(status='Referred').count()
    rejected = Referral.objects.filter(status='Rejected').count()
    serious = Referral.objects.filter(is_serious=True).count()
    by_community = Referral.objects.values('community').annotate(count=Count('id')).order_by('-count')
    by_status = Referral.objects.values('status').annotate(count=Count('id'))

    referrals = referrals[:20]

    return render(request, 'referrals/tracker.html', {
        'referrals': referrals,
        'total': total,
        'sent_count': completed,
        'pending_count': referred,
        'completed': completed,
        'referred': referred,
        'rejected': rejected,
        'serious': serious,
        'by_community': by_community,
        'by_status': by_status,
        'query': query,
        'status_filter': status_filter,
        'added': request.GET.get('added'),
        'done': request.GET.get('done'),
    })

def dashboard_view(request):
    return tracker_view(request)

def send_sms_view(request, referral_id):
    ref = get_object_or_404(Referral, id=referral_id)
    msg = f"CHW Referral {ref.referral_code}: {ref.patient_name} from {ref.community} - {ref.symptoms}. Serious: {ref.is_serious}."
    send_sms("233240352335", msg)
    messages.success(request, f"📱 SMS sent for {ref.patient_name}")
    return redirect('tracker')

# For old code that uses 'tracker' name
tracker = tracker_view