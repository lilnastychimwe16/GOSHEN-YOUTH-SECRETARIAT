from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ZonalObligation, DistrictObligation
from .forms import ZonalObligationForm, DistrictObligationForm

# Create your views here.

# Zonal Obligations Views
@login_required
def zonal_list(request):
    obligations = ZonalObligation.objects.all().order_by('category')
    return render(request, 'obligations/zonal_list.html', {'obligations': obligations})

@login_required
def zonal_create(request):
    if request.method == 'POST':
        form = ZonalObligationForm(request.POST)
        if form.is_valid():
            obligation = form.save(commit=False)
            obligation.created_by = request.user
            obligation.save()
            messages.success(request, 'Zonal obligation created successfully!')
            return redirect('obligations:zonal_list')
    else:
        form = ZonalObligationForm()
    return render(request, 'obligations/zonal_form.html', {'form': form, 'action': 'Create'})

@login_required
def zonal_update(request, pk):
    obligation = get_object_or_404(ZonalObligation, pk=pk)
    if request.method == 'POST':
        form = ZonalObligationForm(request.POST, instance=obligation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Zonal obligation updated successfully!')
            return redirect('obligations:zonal_list')
    else:
        form = ZonalObligationForm(instance=obligation)
    return render(request, 'obligations/zonal_form.html', {'form': form, 'action': 'Update'})

@login_required
def zonal_delete(request, pk):
    obligation = get_object_or_404(ZonalObligation, pk=pk)
    if request.method == 'POST':
        obligation.delete()
        messages.success(request, 'Zonal obligation deleted successfully!')
        return redirect('obligations:zonal_list')
    return render(request, 'obligations/zonal_confirm_delete.html', {'obligation': obligation})

# District Obligations Views
@login_required
def district_list(request):
    obligations = DistrictObligation.objects.all().order_by('district_name')
    return render(request, 'obligations/district_list.html', {'obligations': obligations})

@login_required
def district_create(request):
    if request.method == 'POST':
        form = DistrictObligationForm(request.POST)
        if form.is_valid():
            obligation = form.save(commit=False)
            obligation.created_by = request.user
            obligation.save()
            messages.success(request, 'District obligation created successfully!')
            return redirect('obligations:district_list')
    else:
        form = DistrictObligationForm()
    return render(request, 'obligations/district_form.html', {'form': form, 'action': 'Create'})

@login_required
def district_update(request, pk):
    obligation = get_object_or_404(DistrictObligation, pk=pk)
    if request.method == 'POST':
        form = DistrictObligationForm(request.POST, instance=obligation)
        if form.is_valid():
            form.save()
            messages.success(request, 'District obligation updated successfully!')
            return redirect('obligations:district_list')
    else:
        form = DistrictObligationForm(instance=obligation)
    return render(request, 'obligations/district_form.html', {'form': form, 'action': 'Update'})

@login_required
def district_delete(request, pk):
    obligation = get_object_or_404(DistrictObligation, pk=pk)
    if request.method == 'POST':
        obligation.delete()
        messages.success(request, 'District obligation deleted successfully!')
        return redirect('obligations:district_list')
    return render(request, 'obligations/district_confirm_delete.html', {'obligation': obligation})
