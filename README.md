# IPL Intelligence API

A real-time cricket analytics API built with FastAPI and Python.
Fetches live IPL data from Cricbuzz and predicts match winners.

## Tech Stack
- Python 3.9
- FastAPI
- Requests
- Cricbuzz API (via RapidAPI)

## Endpoints

| Endpoint | Description |
|----------|-------------|
| GET / | Welcome message |
| GET /ipl | Manual IPL matches |
| GET /ipl/live | Live IPL matches |
| GET /ipl/schedule | Upcoming IPL matches |
| GET /ipl/recent | Recently completed matches |
| GET /standings | IPL 2026 points table with win % |
| GET /predict?team1=X&team2=Y | Predict match winner |
| GET /player/{name} | Player details |

## How to Run

1. Install dependencies:
pip install fastapi uvicorn requests

2. Run the server:
uvicorn main:app --reload

3. Open browser at:
http://127.0.0.1:8000

## Example Prediction
GET /predict?team1=PBKS&team2=CSK
{
"predicted_winner": "PBKS",
"confidence": "48.2% edge"
}

## Built by
Parth Pawar — github.com/Parthpawar-06