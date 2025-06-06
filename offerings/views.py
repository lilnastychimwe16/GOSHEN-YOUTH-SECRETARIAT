from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FreewillOffering
from .forms import FreewillOfferingForm

# Create your views here.

@login_required
def offering_list(request):
    offerings = FreewillOffering.objects.all().order_by('-week_start_date')
    return render(request, 'offerings/offering_list.html', {'offerings': offerings})

@login_required
def offering_create(request):
    if request.method == 'POST':
        form = FreewillOfferingForm(request.POST)
        if form.is_valid():
            offering = form.save(commit=False)
            offering.created_by = request.user
            offering.save()
            messages.success(request, 'Freewill offering recorded successfully!')
            return redirect('offerings:list')
    else:
        form = FreewillOfferingForm()
    return render(request, 'offerings/offering_form.html', {'form': form, 'action': 'Create'})

@login_required
def offering_update(request, pk):
    offering = get_object_or_404(FreewillOffering, pk=pk)
    if request.method == 'POST':
        form = FreewillOfferingForm(request.POST, instance=offering)
        if form.is_valid():
            form.save()
            messages.success(request, 'Freewill offering updated successfully!')
            return redirect('offerings:list')
    else:
        form = FreewillOfferingForm(instance=offering)
    return render(request, 'offerings/offering_form.html', {'form': form, 'action': 'Update'})

@login_required
def offering_delete(request, pk):
    offering = get_object_or_404(FreewillOffering, pk=pk)
    if request.method == 'POST':
        offering.delete()
        messages.success(request, 'Freewill offering deleted successfully!')
        return redirect('offerings:list')
    return render(request, 'offerings/offering_confirm_delete.html', {'offering': offering})
