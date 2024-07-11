import pandas as pd

data_frame = pd.read_csv("data/results.csv")

games = data_frame.to_dict(orient="records")

teams = {}

count = 0

for game in games:
    home = game["home_team"]
    away = game["away_team"]
    home_goals = game["home_score"]
    away_goals = game["away_score"]
    
    if pd.isna(home_goals) or pd.isna(away_goals):
        continue
    
    if home not in teams:
        teams.update({home: {"name": home, "games": 0, "goals_for": 0, "goals_against": 0}})
        
    if away not in teams:
        teams.update({away: {"name": away, "games": 0, "goals_for": 0, "goals_against": 0}})
    
    teams[home]["games"] += 1
    teams[away]["games"] += 1
    
    teams[home]["goals_for"] += home_goals
    teams[away]["goals_for"] += away_goals
    
    teams[away]["goals_against"] += home_goals
    teams[home]["goals_against"] += away_goals
    
    count += 1
    
    
    
# reset_index() to have the country names as indexes btw
teams_data_frame = pd.DataFrame.from_dict(teams, orient='index')

print(count)


teams_data_frame.to_csv("data/teams.csv", index=False)