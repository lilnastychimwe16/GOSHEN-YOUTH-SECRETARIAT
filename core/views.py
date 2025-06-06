from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from offerings.models import FreewillOffering
from obligations.models import ZonalObligation, DistrictObligation

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def dashboard(request):
    # Get the latest and previous freewill offerings
    offerings = FreewillOffering.objects.all().order_by('-week_start_date')[:2]
    latest_offering = offerings[0] if offerings else None
    previous_offering = offerings[1] if len(offerings) > 1 else None
    
    # Get all zonal obligations
    zonal_obligations = ZonalObligation.objects.all()
    
    # Get all district obligations
    district_obligations = DistrictObligation.objects.all()
    
    context = {
        'latest_offering': latest_offering,
        'previous_offering': previous_offering,
        'zonal_obligations': zonal_obligations,
        'district_obligations': district_obligations,
    }
    
    return render(request, 'core/dashboard.html', context)
