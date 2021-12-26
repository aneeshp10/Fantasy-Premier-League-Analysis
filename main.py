import requests
import pandas as pd
import numpy as np

req = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')
json_resp = req.json()
pd.options.display.max_columns = None
json_resp.keys()

# creating dataframs out of the keys
element_dataframe = pd.DataFrame(json_resp['elements'])
element_types_dataframe = pd.DataFrame(json_resp['element_types'])
teams_dataframe = pd.DataFrame(json_resp['teams'])

tmp_elements_dataframe = element_dataframe[['web_name', 'team', 'element_type', 'selected_by_percent', 'now_cost','minutes', 'transfers_in'
                                           , 'transfers_out', 'value_season', 'total_points']]

# this updates the position to be either keeper, midfielder, forward, defender
tmp_elements_dataframe['position'] = tmp_elements_dataframe.element_type.map(element_types_dataframe.set_index('id').singular_name)

# this updates the team from a number to the team name
tmp_elements_dataframe['team'] = tmp_elements_dataframe.team.map(teams_dataframe.set_index('id').name)

# create new values column
tmp_elements_dataframe['player_value'] = tmp_elements_dataframe.value_season.astype(float)
tmp_elements_dataframe = tmp_elements_dataframe.sort_values('player_value', ascending=False)
tmp_elements_dataframe = tmp_elements_dataframe.loc[tmp_elements_dataframe.player_value > 0]

# pivot table based on positions
position_pivot = tmp_elements_dataframe.pivot_table(index='position', values='player_value',aggfunc=np.mean).reset_index()
position_pivot.sort_values('player_value', ascending=False)

team_pivot = tmp_elements_dataframe.pivot_table(index='team', values='player_value',aggfunc=np.mean).reset_index()
team_pivot.sort_values('player_value', ascending=False)

#tmp_elements_dataframe.head(50)

