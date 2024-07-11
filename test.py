import pandas as pd

data_frame = pd.read_csv("data/results.csv")

games = data_frame.to_dict(orient="records")

teams = {}

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
    
best = ("???", -1)
worst = ("???", 1000)
    
for team in teams.values():
    avg_goals = round(team["goals_for"] / team["games"], 2)
    avg_conceded = round(team["goals_against"] / team["games"], 2)
    
    team["average_goals_per_game"] = avg_goals
    team["average_conceded_per_game"] = avg_conceded
    
    if(avg_goals > best[1]):
        best = (team["name"], avg_goals)
        
    if(avg_conceded < worst[1]):
        worst = (team["name"], avg_conceded)
    

print(best)
print(worst)

teams_data_frame = pd.DataFrame.from_dict(teams, orient='index')

teams_data_frame.to_csv("data/teams.csv", index=False)