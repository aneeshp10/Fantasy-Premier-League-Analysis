import requests
import numpy as np
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# add up all the points collected by each man city, liverpool, chelsea, and arsenal player
#player_points = {"Arsenal": 0, "Aston Villa": 0, "Brentford": 0, "Chelsea": 0, "Man City": 0, "Liverpool": 0,}
#player_cost = {"Man City": 0, "Liverpool": 0, "Chelsea": 0, "Arsenal": 0}

req = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')
json_resp = req.json()
players = json_resp['elements']
player_points = {}
player_cost = {}
all_teams = []
team_names = json_resp['teams']
for i in range(len(team_names)):
    all_teams.append(team_names[i]['name'])
player_points = {key: 0 for key in all_teams}
player_cost = {key: 0 for key in all_teams}

team_ids = [i + 1 for i in range(20)]


for i in range(1, len(players)):
    if players[i]['team'] == ars_id:
        player_points["Arsenal"] += players[i]['total_points']
        player_cost["Arsenal"] += round(float(players[i]['now_cost']) / 10, 2)
    
    elif players[i]['team'] == city_id:
        player_points["Man City"] += players[i]['total_points']
        player_cost["Man City"] += round(float(players[i]['now_cost']) / 10, 2)
    
    elif players[i]['team'] == city_id:
        player_points["Man City"] += players[i]['total_points']
        player_cost["Man City"] += round(float(players[i]['now_cost']) / 10, 2)
        
    elif players[i]['team'] == liv_id:
        player_points["Liverpool"] += players[i]['total_points']
        player_cost["Liverpool"] += round(float(players[i]['now_cost']) / 10, 2)
        
    elif players[i]['team'] == che_id:
        player_points["Chelsea"] += players[i]['total_points']
        player_cost["Chelsea"] += float(players[i]['now_cost']) / 10
#print(player_points)
#print(player_cost)

# plotting
xAxis = np.arange(4)


f = plt.figure()
f.set_figwidth(10)
f.set_figheight(7)
p_list = player_points.values()
c_list = player_cost.values()

plt.bar(xAxis, p_list, color='pink', width=0.2, label='Points')
plt.bar(xAxis + 0.2, c_list, color='violet', width=0.2, label='Cost')
plt.xticks(xAxis + 0.2/2, player_points.keys())
plt.xlabel('Club')
plt.ylabel('Points and Cost')
plt.legend()
