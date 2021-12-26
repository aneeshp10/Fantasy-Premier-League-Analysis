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
    if players[i]['team'] == 1:
        player_points["Arsenal"] += players[i]['total_points']
        player_cost["Arsenal"] += round(float(players[i]['now_cost']) / 10, 2)
    
    
    elif players[i]['team'] == 2:
        player_points["Aston Villa"] += players[i]['total_points']
        player_cost["Aston Villa"] += round(float(players[i]['now_cost']) / 10, 2)
        
        
    elif players[i]['team'] == 3:
        player_points["Brentford"] += players[i]['total_points']
        player_cost["Brentford"] += round(float(players[i]['now_cost']) / 10, 2)
    
    
    
    elif players[i]['team'] == 4:
        player_points["Brighton"] += players[i]['total_points']
        player_cost["Brighton"] += round(float(players[i]['now_cost']) / 10, 2)
    
    
    elif players[i]['team'] == 5:
        player_points["Brentford"] += players[i]['total_points']
        player_cost["Brentford"] += round(float(players[i]['now_cost']) / 10, 2)
        
    
    elif players[i]['team'] == 6:
        player_points["Chelsea"] += players[i]['total_points']
        player_cost["Chelsea"] += float(players[i]['now_cost']) / 10
    
    
    elif players[i]['team'] == 7:
        player_points["Crystal Palace"] += players[i]['total_points']
        player_cost["Crystal Palace"] += round(float(players[i]['now_cost']) / 10, 2)
    
    
    elif players[i]['team'] == 8:
        player_points["Everton"] += players[i]['total_points']
        player_cost["Everton"] += round(float(players[i]['now_cost']) / 10, 2)
    
    
    
    elif players[i]['team'] == 9:
        player_points["Leicester"] += players[i]['total_points']
        player_cost["Leicester"] += round(float(players[i]['now_cost']) / 10, 2)
    
    
    
    elif players[i]['team'] == 10:
        player_points["Leeds"] += players[i]['total_points']
        player_cost["Leeds"] += round(float(players[i]['now_cost']) / 10, 2)
        
    
    
    elif players[i]['team'] == 11:
        player_points["Liverpool"] += players[i]['total_points']
        player_cost["Liverpool"] += round(float(players[i]['now_cost']) / 10, 2)
    
    
    
    elif players[i]['team'] == 12:
        player_points["Man City"] += players[i]['total_points']
        player_cost["Man City"] += round(float(players[i]['now_cost']) / 10, 2)
    
    
    
    elif players[i]['team'] == 13:
        player_points["Man Utd"] += players[i]['total_points']
        player_cost["Man Utd"] += round(float(players[i]['now_cost']) / 10, 2)
        
    
    
    elif players[i]['team'] == 14:
        player_points["Newcastle"] += players[i]['total_points']
        player_cost["Newcastle"] += round(float(players[i]['now_cost']) / 10, 2)
    
    
    elif players[i]['team'] == 15:
        player_points["Norwich"] += players[i]['total_points']
        player_cost["Norwich"] += round(float(players[i]['now_cost']) / 10, 2)
        
        
    elif players[i]['team'] == 16:
        player_points["Southampton"] += players[i]['total_points']
        player_cost["Southampton"] += round(float(players[i]['now_cost']) / 10, 2)
    
    
    elif players[i]['team'] == 17:
        player_points["Spurs"] += players[i]['total_points']
        player_cost["Spurs"] += round(float(players[i]['now_cost']) / 10, 2)
        
        
    elif players[i]['team'] == 18:
        player_points["Watford"] += players[i]['total_points']
        player_cost["Watford"] += round(float(players[i]['now_cost']) / 10, 2)
        
        
    elif players[i]['team'] == 19:
        player_points["West Ham"] += players[i]['total_points']
        player_cost["West Ham"] += round(float(players[i]['now_cost']) / 10, 2)
    
    elif players[i]['team'] == 20:
        player_points["Wolves"] += players[i]['total_points']
        player_cost["Wolves"] += round(float(players[i]['now_cost']) / 10, 2)
        
 

print(player_points)
