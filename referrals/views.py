from django.shortcuts import render
from .models import Referral

def home(request):
    referrals = Referral.objects.all().order_by('-id')
    return render(request, 'referrals/home.html', {'referrals': referrals})