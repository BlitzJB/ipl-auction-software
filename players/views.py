from django.shortcuts import render
import numpy as np
from .models import Player
from django.http import JsonResponse


pool_name_map = {
    1: "MARQUEE SET",
    2: "BATSMEN 1",
    3: "ALL ROUNDERS 1",
    4: "WICKET KEEPERS 1",
    5: "FAST BOWLERS 1",
    6: "SPIN BOWLERS 1",
    7: "BATSMEN 2",
    8: "WICKET KEEPERS 2",
    9: "ALL ROUNDERS 2",
    10: "FAST BOWLERS 2",
    11: "SPIN BOWLERS 2",
    12: "ALL ROUNDERS 3",
    13: "BATSMEN 3",
    14: "ALL ROUNDERS 4"
}

pool_code_map = {
    1: "MS",
    2: "BA1",
    3: "AR1",
    4: "WK1",
    5: "FB1",
    6: "SB1",
    7: "BA2",
    8: "WK2",
    9: "AR2",
    10: "FB2",
    11: "SB2",
    12: "AR3",
    13: "BA3",
    14: "AR4"
}

rtm_use = {"MI":0, "CSK":0, "RCB":0, "KKR":0, "SRH":0, "DC":0, "RR":0, "PBKS":0}

lst=[]
for i in list(pool_code_map.keys()):
    j = np.array(Player.objects.filter(setNo=i))
    if j.any():
        np.random.shuffle(j)
    lst.extend(j)

def player(request, pk):
    if request.method=='GET':
        try:
            newpool = True if lst[int(pk)-1].setNo!=lst[int(pk)-2].setNo or int(pk)==1 else False
            output = {
                'player': lst[int(pk)-1],
                'id':pk,
                'pool': {
                    'poolName': pool_name_map[lst[int(pk)-1].setNo],
                    'poolCode': pool_code_map[lst[int(pk)-1].setNo],
                    'isNewPool': newpool
                },
                'rtm': lst[int(pk)-1].prev_team if rtm_use[lst[int(pk)-1].prev_team.upper()]<3 else None
            }
            return render(request, 'index.html', output)
        except IndexError:
            return JsonResponse({"error": "Player not found"})
    elif request.method=='POST':
        print(request.POST)    
