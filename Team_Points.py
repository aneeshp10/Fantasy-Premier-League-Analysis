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
my_points = []
avg_points = []
highest_points = []
for i in range(1, latest_gw):
    my_points.append(my_gw["GW:" + str(i)]['entry_history']['points'])
    avg_points.append(events[i - 1]['average_entry_score'])
    highest_points.append(events[i - 1]['highest_score'])
print(avg_points)


# plotting
fig, ax1 = plt.subplots(1,1)

xAxis = np.arange(1, latest_gw)
ax1.plot(xAxis, my_points, color='firebrick', label='My FPL')
ax1.plot(xAxis, avg_points, color='springgreen', label='Overall Avg.')
ax1.plot(xAxis, highest_points, color='darksalmon', label='Overall Max.')
ax1.set_xlabel('GW No.')
ax1.set_ylabel('Points')
ax1.legend(loc='best', frameon=True, prop={'size':6})
