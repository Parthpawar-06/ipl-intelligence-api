
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





    return 
            



    

