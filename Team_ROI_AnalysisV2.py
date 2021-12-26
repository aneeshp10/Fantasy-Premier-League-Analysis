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

player_index = 0
print(hi)
for i in range (1, 3):
    points_sum = 0
    cost_sum = 0
    print(hi)
    while players[player_index]['team'] == i:
        points_sum += players[i]['total_points']
        cost_sum += float(players[i]['now_cost']) / 10
        player_index = player_index + 1
        if players[i]['team'] != i:
            break
    player_points[i] = points_sum
    player_cost[i] = cost_sum
    
print(player_points)
