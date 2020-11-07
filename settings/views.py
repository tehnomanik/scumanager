from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from players.models import Player


# SETTINGS HOME PAGE
@login_required(login_url='account-login')
def settingsHome(request):
    page_title = " - Settings"
    context = {'page_title': page_title}
    return render(request, 'settings/settings_home.html', context)

# SETTINGS HOME PAGE
@login_required(login_url='account-login')
def settingsRefreshPlayers(request):
    item = "NEMA"
    if request.method == "POST":
        log = request.POST.get('log')
        players = []
        rows_created = 0
        rows_updated = 0

        for item in log.splitlines():
            if "' logged in" in item:          
                steam_id = ""
                ingame_name = ""
                server_id = ""

                item = item.split("'")

                #item = item[2].split(':')
                steam_id = item[1].split(':')[0].split(' ')[1]
                #item = item[1].split('(')        
                ingame_name = item[1].split(':')[1].split('(')[0]
                server_id = item[1].split(':')[1].split('(')[1][:-1]

                if server_id.isdigit():
                    obj = Player.objects.filter(steam_id=steam_id).first()
                    if obj is None:
                        player = Player(steam_id=steam_id, ingame_name=ingame_name, server_id=int(server_id))
                        player.save()
                        rows_created += 1
                        #line = str(steam_id) + '###' + str(ingame_name) + '###' + str(server_id)
                        #players.append(line)
                    else:
                        if obj.ingame_name != ingame_name or obj.server_id != int(server_id):
                            obj.server_id = int(server_id)
                            obj.save()
                            rows_updated += 1
        item = players

        messages.success(request, 'Players created: ' + str(rows_created) + '  Players updated: ' + str(rows_updated) )

    page_title = " - Refresh player list"
    context = {'page_title': page_title, 'item': item}
    return render(request, 'settings/settings_login_refresh.html', context)