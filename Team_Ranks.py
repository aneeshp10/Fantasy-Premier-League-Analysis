import requests
import numpy as np
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

tid = 2339775
latest_gw = 19
my_gw = {}
fpl_static = "https://fantasy.premierleague.com/api/bootstrap-static/"

for i in range(1, latest_gw + 1):
    fpl_url = "https://fantasy.premierleague.com/api/entry/" + str(tid) + "/event/" + str(i) + "/picks/"
    r = requests.get(fpl_url)
    tmp_dict = {"GW:" + str(i) : r.json()}
    my_gw.update(tmp_dict)

static_resp = requests.get(fpl_static)
events = static_resp.json()['events']

# add my points, average points, highest points per week
my_gw_rank = []
my_overall_rank = []
for i in range(1, latest_gw):
    my_gw_rank.append(my_gw["GW:" + str(i)]['entry_history']['rank'])
    my_overall_rank.append(my_gw["GW:" + str(i)]['entry_history']['overall_rank'])

# plotting
xAxis = np.arange(1, latest_gw)


f = plt.figure()
f.set_figwidth(10)
f.set_figheight(7)

plt.bar(xAxis, my_gw_rank, color='slateblue', width=0.5, label='My Gameweek Rank')
plt.bar(xAxis + 0.5, my_overall_rank, color='darkturquoise', width=0.5, label='My Overall Rank')
plt.xticks(xAxis + 0.5/2,xAxis)
plt.xlabel('GW No.')
plt.ylabel('Rank')
plt.legend()

