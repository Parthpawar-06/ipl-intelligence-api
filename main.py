
from fastapi import FastAPI
import requests
app  = FastAPI()
@app.get("/")
def home():
    return {"message" : "I have started"}

@app.get("/ipl")
def ipl_matches():
    return [{"team1":"MI" ,"team2":"CSK","Venue":"WANKHEDE"},
            {"team1":"KKR" ,"team2":"RR","Venue":"EDEN GARDENS"},
            {"team1":"DC" ,"team2":"PBKS","Venue":"FEROZ SHAH KOTLA"}]

@app.get("/player")
def player_details():
    return {"name":"Virat","team":"RCB","ROLE":"BATTER"}

@app.get("/player/{name}")
def get_player(name):
    return {"player":name,"message": "Stats coming soon"}

@app.get("/live")
def live_match():
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"
    response = requests.get(url,headers={"x-rapidapi-key":"68ea60a1fdmshc7b501fac7d21d8p126958jsnc0ca635fdc0d"})
    return response.json()

@app.get("/ipl/live")
def ipl_live():
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"
    headers = {"x-rapidapi-key": "68ea60a1fdmshc7b501fac7d21d8p126958jsnc0ca635fdc0d"}
    response = requests.get(url, headers=headers)
    data = response.json()

    ipl_matches = []
    for i in data.get("typeMatches", []):
        for a in i.get("seriesMatches", []):
            series = a.get("seriesAdWrapper", {})
            series_name = series.get("seriesName", "")
            if "Indian Premier League" in series_name:
                for b in series.get("matches", []):
                    info = b.get("matchInfo", {})
                    ipl_matches.append({
                        "match": info.get("matchDesc", ""),
                        "team1": info.get("team1", {}).get("teamName", ""),
                        "team2": info.get("team2", {}).get("teamName", ""),
                        "status": info.get("status", ""),
                        "venue": info.get("venueInfo", {}).get("ground", ""),
                        "score": b.get("matchScore", {})
                    })

    return {"total": len(ipl_matches), "matches": ipl_matches}            

@app.get("/ipl/schedule")
def schedule():
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/upcoming"
    headers = {"x-rapidapi-key": "68ea60a1fdmshc7b501fac7d21d8p126958jsnc0ca635fdc0d"}
    response = requests.get(url,headers = headers)
    data = response.json()
    upcoming_matches = []

    for i in data.get("typeMatches",[]):
        for a in i.get("seriesMatches",[]):
            series = a.get("seriesAdWrapper",{})
            series_name = series.get("seriesName","")
            if "Indian Premier League" in series_name:
                for b in series.get("matches","[]"):
                    info = b.get("matchInfo", {})
                    upcoming_matches.append({
                        "match": info.get("matchDesc", ""),
                        "team1": info.get("team1", {}).get("teamName", ""),
                        "team2": info.get("team2", {}).get("teamName", ""),
                        "status": info.get("status", ""),
                        "venue": info.get("venueInfo", {}).get("ground", ""),
                        "score": b.get("matchScore", {})
                    })
    return {"total": len(upcoming_matches), "matches": upcoming_matches}

@app.get("/ipl/recent")
def recent():

    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"
    headers = {"x-rapidapi-key": "68ea60a1fdmshc7b501fac7d21d8p126958jsnc0ca635fdc0d"}
    response = requests.get(url,headers = headers)
    data = response.json()
    recent_matches = []
    
    for i in data.get("typeMatches",[]):
        for a in i.get("seriesMatches",[]):
            series = a.get("seriesAdWrapper",{})
            series_name = series.get("seriesName","")
            if "Indian Premier League" in series_name:
                for b in series.get("matches",[]):
                    info = b.get("matchInfo", {})
                    recent_matches.append({
                        "match": info.get("matchDesc", ""),
                        "team1": info.get("team1", {}).get("teamName", ""),
                        "team2": info.get("team2", {}).get("teamName", ""),
                        "status": info.get("status", ""),
                        "venue": info.get("venueInfo", {}).get("ground", ""),
                        "score": b.get("matchScore", {})
                    })
    return {"total": len(recent_matches) , "recent_matches": recent_matches}


@app.get("/standings")
def standings():

    url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/series/9241/points-table"            
    headers = {"x-rapidapi-key": "68ea60a1fdmshc7b501fac7d21d8p126958jsnc0ca635fdc0d"}
    response = requests.get(url,headers = headers)
    data = response.json()
    teams = []

    for i in data.get("pointsTable",[]):
        for a in i.get("pointsTableInfo",[]):
            teams.append({
                "team": a.get("teamName",""),
                "fullname": a.get("teamFullName",""),
                "played":a.get("matchesPlayed"),
                "won": a.get("matchesWon"),
                "points":a.get("points"),
                "nrr":a.get("nrr"),
                "win_pct": round(a.get("matchesWon", 0) / a.get("matchesPlayed", 1) * 100, 1)
            })

    return {"standings":teams}

@app.get("/predict")
def prediction(team1: str, team2: str):

    url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/series/9241/points-table"            
    headers = {"x-rapidapi-key": "68ea60a1fdmshc7b501fac7d21d8p126958jsnc0ca635fdc0d"}
    response = requests.get(url,headers = headers)
    data = response.json()

    team1_pct = 0
    team2_pct = 0

    for i in data.get("pointsTable", []):
        for a in i.get("pointsTableInfo", []):
            name = a.get("teamName", "")
            pct = round(a.get("matchesWon", 0) / a.get("matchesPlayed", 1) * 100, 1)
            if name == team1:
                team1_pct = pct
            if name == team2:
                team2_pct = pct


    confidence = 0
    winner = "NA"
    if(team1_pct>team2_pct):
        confidence = round(team1_pct-team2_pct,1)
        winner = team1
    else:
        confidence = round(team2_pct-team1_pct,1)
        winner = team2

    return {
        "team1": team1,
        "team2": team2,
        "team1_win_pct": team1_pct,
        "team2_win_pct": team2_pct,
        "predicted_winner": winner,
        "confidence": f"{confidence}% edge"
    }


    



    

    

