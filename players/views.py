from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .filters import *
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

####################################################
#  PLAYERS START

# PLAYERS HOME PAGE, LISTS ALL PLAYERS
@login_required(login_url='account-login')
def playersHome(request):
    players = Player.objects.order_by(Lower('ingame_name')).all()

    myFilter = PlayerFilter(request.GET, queryset = players)

    players = myFilter.qs

    page_title = " - Players"
    context = {'page_title': page_title,'item':players, 'myFilter':myFilter}
    return render(request, 'players/players_home.html', context)

# CREATE NEW PLAYER, OPENS FORM playerForm() from forms.py
@login_required(login_url='account-login')
def createPlayer(request):
    form = playerForm()

    if request.method == 'POST':
        form = playerForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            name = form.cleaned_data.get('ingame_name')
            messages.success(request, 'New player created: ' + name)
            return redirect('players-home')

    page_title = " - Add new player"
    context = {'page_title': page_title,'form': form}
    return render(request, 'players/players_form.html', context)

# UPDATE PLAYER, OPENS FORM playerForm() from forms.py
@login_required(login_url='account-login')
def updatePlayer(request, pk):
    player = Player.objects.get(id=pk)
    form = playerForm(instance=player)

    if request.method == 'POST':
        form = playerForm(request.POST, instance=player)
        if form.is_valid():
            form.save(request.user)
            name = form.cleaned_data.get('ingame_name')
            messages.success(request, 'Player info updated: ' + name)
            return redirect('players-home')

    page_title = " - Update player info"
    context = {'page_title': page_title,'form': form}
    return render(request, 'players/players_form.html', context)

# DELETE PLAYER, OPENS html page players_delete.html
@login_required(login_url='account-login')
def deletePlayer(request, pk):
    player = Player.objects.get(id=pk)

    if request.method == "POST":
        name = player.ingame_name
        player.delete()
        messages.success(request, 'Player deleted: ' + str(name))
        return redirect('players-home')

    page_title = " - Delete Player"
    context = {'page_title': page_title,'item': player}
    return render(request, 'players/players_delete.html', context)

#  PLAYERS END
####################################################

####################################################
#  SQUADS START

# SQAD HOME PAGE, LISTS ALL SQADS
@login_required(login_url='account-login')
def squadHome(request):
    squads_all = Squad.objects.order_by(Lower('ingame_name')).all()
    myFilter = SquadFilter(request.GET, queryset = squads_all)
    squads_all = myFilter.qs
    
    page_title = " - Squads"
    context = {'page_title': page_title,'item':squads_all,'myFilter':myFilter}
    return render(request, 'players/squad_home.html', context)

# CREATE NEW SQUAD, OPENS FORM squadForm() from forms.py
@login_required(login_url='account-login')
def createSquad(request):
    form = squadForm()

    if request.method == 'POST':
        form = squadForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            name = form.cleaned_data.get('ingame_name')
            messages.success(request, 'New squad created: ' + name)
            return redirect('squad-home')

    page_title = " - Add new squad"
    context = {'page_title': page_title,'form': form}
    return render(request, 'players/squad_form.html', context)

# UPDATE SQUAD, OPENS FORM squadForm() from forms.py
@login_required(login_url='account-login')
def updateSquad(request, pk):
    squad = Squad.objects.get(id=pk)
    form = squadForm(instance=squad)

    if request.method == 'POST':
        form = squadForm(request.POST, instance=squad)
        if form.is_valid():
            form.save(request.user)
            name = form.cleaned_data.get('ingame_name')
            messages.success(request, 'Squad info updated: ' + name)
            return redirect('squad-home')

    page_title = " - Update squad info"
    context = {'page_title': page_title,'form': form}
    return render(request, 'players/squad_form.html', context)

# DELETE SQUAD, OPENS html page squad_delete.html
@login_required(login_url='account-login')
def deleteSquad(request, pk):
    squad = Squad.objects.get(id=pk)

    if request.method == "POST":
        name = squad.ingame_name
        squad.delete()
        messages.success(request, 'Squad deleted: ' + str(name))
        return redirect('squad-home')

    page_title = " - Delete Squad"
    context = {'page_title': page_title,'item': squad}
    return render(request, 'players/squad_delete.html', context)

#  SQUADS END
####################################################


####################################################
#  DONATIONS START

# DONATION HOME PAGE, LISTS ALL DONATIONS
@login_required(login_url='account-login')
def donationHome(request):
    donations = Donation.objects.order_by('-donation_date').all()
    myFilter = DonationFilter(request.GET, queryset = donations)
    donations = myFilter.qs

    page_title = " - Donations"
    context = {'page_title': page_title,'item': donations,'myFilter':myFilter}
    return render(request, 'players/donation_home.html', context)

# CREATE NEW DONATION, OPENS FORM donationForm() from forms.py
@login_required(login_url='account-login')
def createDonation(request):
    form = donationForm()

    if request.method == 'POST':
        form = donationForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            messages.success(request, 'Donation saved.')
            return redirect('donation-home')

    page_title = " - Add new donation"
    context = {'page_title': page_title,'form': form}
    return render(request, 'players/donation_form.html', context)

# UPDATE DONATION, OPENS FORM donationForm() from forms.py
@login_required(login_url='account-login')
def updateDonation(request, pk):
    donation = Donation.objects.get(id=pk)
    form = donationForm(instance=donation)

    if request.method == 'POST':
        form = donationForm(request.POST, instance=donation)
        if form.is_valid():
            form.save(request.user)
            messages.success(request, 'Donation info updated.')
            return redirect('donation-home')

    page_title = " - Update donation info"
    context = {'page_title': page_title,'form': form}
    return render(request, 'players/donation_form.html', context)

# DELETE DONATION, OPENS html page donation_delete.html
@login_required(login_url='account-login')
def deleteDonation(request, pk):
    donation = Donation.objects.get(id=pk)

    if request.method == "POST":
        donation.delete()
        messages.success(request, 'Donation deleted: ' + str(donation))
        return redirect('donation-home')

    page_title = " - Delete Donation"
    context = {'page_title': page_title,'item': donation}
    return render(request, 'players/donation_delete.html', context)

#  DONATIONS END
####################################################


####################################################
#  VEHICLES START

# VEHICLES HOME PAGE, LISTS ALL VEHICLES
@login_required(login_url='account-login')
def vehicleHome(request):
    vehicles = Vehicle.objects.all()
    myFilter = VehicleFilter(request.GET, queryset = vehicles)
    vehicles = myFilter.qs
    
    page_title = " - Vehicles"
    context = {'page_title': page_title,'item':vehicles,'myFilter':myFilter}
    return render(request, 'players/vehicle_home.html', context)

# CREATE NEW VEHICLE, OPENS FORM vehicleForm() from forms.py
@login_required(login_url='account-login')
def createVehicle(request):
    form = vehicleForm()

    if request.method == 'POST':
        form = vehicleForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            messages.success(request, 'New vehicle added.')
            return redirect('vehicle-home')

    page_title = " - Add new vehicle"
    context = {'page_title': page_title,'form': form}
    return render(request, 'players/vehicle_form.html', context)

# UPDATE VEHICLE, OPENS FORM vehicleForm() from forms.py
@login_required(login_url='account-login')
def updateVehicle(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    form = vehicleForm(instance=vehicle)

    if request.method == 'POST':
        form = vehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save(request.user)
            messages.success(request, 'Vehicle info updated.')
            return redirect('vehicle-home')

    page_title = " - Update vehicle info"
    context = {'page_title': page_title,'form': form}
    return render(request, 'players/vehicle_form.html', context)

# DELETE VEHICLE, OPENS html page vehicle_delete.html
@login_required(login_url='account-login')
def deleteVehicle(request, pk):
    vehicle = Vehicle.objects.get(id=pk)

    if request.method == "POST":
        vehicle.delete()
        messages.success(request, 'Vehicle deleted.')
        return redirect('vehicle-home')

    page_title = " - Delete Vehicle"
    context = {'page_title': page_title,'item': vehicle}
    return render(request, 'players/vehicle_delete.html', context)



#  VEHICLES END
####################################################


####################################################
#  CASES START

# CASES HOME PAGE, LISTS ALL CASES
@login_required(login_url='account-login')
def caseHome(request):
    cases = Case.objects.order_by('-case_date').all()
    myFilter = CaseFilter(request.GET, queryset = cases)
    cases = myFilter.qs


    page_title = " - Cases"
    context = {'page_title': page_title,'item':cases, 'myFilter':myFilter}
    return render(request, 'players/case_home.html', context)

# CREATE NEW CASE, OPENS FORM caseForm() from forms.py
@login_required(login_url='account-login')
def createCase(request):
    form = caseForm()

    if request.method == 'POST':
        form = caseForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            messages.success(request, 'New case created.')
            return redirect('case-home')

    page_title = " - Add new case"
    context = {'page_title': page_title,'form': form}
    return render(request, 'players/case_form.html', context)

# UPDATE CASE, OPENS FORM caseForm() from forms.py
@login_required(login_url='account-login')
def updateCase(request, pk):
    case = Case.objects.get(id=pk)
    form = caseForm(instance=case)

    if request.method == 'POST':
        form = caseForm(request.POST, instance=case)
        if form.is_valid():
            form.save(request.user)
            messages.success(request, 'Case data updated.')
            return redirect('case-home')

    page_title = " - Update case info"
    context = {'page_title': page_title,'form': form}
    return render(request, 'players/case_form.html', context)

# DELETE CASE, OPENS html page case_delete.html
@login_required(login_url='account-login')
def deleteCase(request, pk):
    case = Case.objects.get(id=pk)

    if request.method == "POST":
        case.delete()
        messages.success(request, 'Case deleted.')
        return redirect('case-home')

    page_title = " - Delete Case"
    context = {'page_title': page_title,'item': case}
    return render(request, 'players/case_delete.html', context)

#  CASES END
####################################################