import os
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional, Dict, Any

app = FastAPI(title="IPL Encyclopedia API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------------------------------
# Seed Data (can be migrated to DB later)
# ------------------------------------------------------------------
TEAMS: List[Dict[str, Any]] = [
    {
        "id": "csk",
        "name": "Chennai Super Kings",
        "shortName": "CSK",
        "logo": "https://upload.wikimedia.org/wikipedia/en/2/2f/Chennai_Super_Kings_Logo.svg",
        "colors": ["#f9cd05", "#1e1e1e"],
        "homeGround": "M. A. Chidambaram Stadium, Chennai",
        "owners": ["Chennai Super Kings Cricket Ltd"],
        "captain": "Ruturaj Gaikwad",
        "headCoach": "Stephen Fleming",
        "supportStaff": [
            {"name": "Eric Simons", "role": "Bowling Coach"},
            {"name": "Michael Hussey", "role": "Batting Coach"},
        ],
        "website": "https://www.chennaisuperkings.com/",
        "social": {
            "twitter": "https://twitter.com/ChennaiIPL",
            "instagram": "https://instagram.com/chennaiipl",
            "facebook": "https://facebook.com/TheChennaiSuperKings"
        },
        "achievements": [
            "IPL Champions: 2010, 2011, 2018, 2021, 2023",
            "Most playoff appearances"
        ],
        "roster": {
            "batsmen": ["Ruturaj Gaikwad", "Ajinkya Rahane"],
            "bowlers": ["Deepak Chahar", "Matheesha Pathirana"],
            "allRounders": ["Ravindra Jadeja", "Moeen Ali"],
            "wicketkeepers": ["MS Dhoni"]
        }
    },
    {
        "id": "mi",
        "name": "Mumbai Indians",
        "shortName": "MI",
        "logo": "https://upload.wikimedia.org/wikipedia/en/2/25/Mumbai_Indians_Logo.svg",
        "colors": ["#004ba0", "#d4af37"],
        "homeGround": "Wankhede Stadium, Mumbai",
        "owners": ["Indiawin Sports Pvt. Ltd (Reliance Industries)"],
        "captain": "Hardik Pandya",
        "headCoach": "Mark Boucher",
        "supportStaff": [
            {"name": "Lasith Malinga", "role": "Bowling Coach"},
            {"name": "Kieron Pollard", "role": "Batting Coach"},
        ],
        "website": "https://www.mumbaiindians.com/",
        "social": {
            "twitter": "https://twitter.com/mipaltan",
            "instagram": "https://instagram.com/mumbaiindians",
            "facebook": "https://facebook.com/mumbaiindians"
        },
        "achievements": [
            "IPL Champions: 2013, 2015, 2017, 2019, 2020"
        ],
        "roster": {
            "batsmen": ["Rohit Sharma", "Suryakumar Yadav"],
            "bowlers": ["Jasprit Bumrah", "Piyush Chawla"],
            "allRounders": ["Hardik Pandya", "Romario Shepherd"],
            "wicketkeepers": ["Ishan Kishan"]
        }
    },
    {
        "id": "rcb",
        "name": "Royal Challengers Bengaluru",
        "shortName": "RCB",
        "logo": "https://upload.wikimedia.org/wikipedia/en/2/2f/Royal_Challengers_Bangalore_Logo.svg",
        "colors": ["#da1212", "#000000"],
        "homeGround": "M. Chinnaswamy Stadium, Bengaluru",
        "owners": ["United Spirits"],
        "captain": "Faf du Plessis",
        "headCoach": "Andy Flower",
        "supportStaff": [
            {"name": "Adam Griffith", "role": "Bowling Coach"}
        ],
        "website": "https://www.royalchallengers.com/",
        "social": {
            "twitter": "https://twitter.com/RCBTweets",
            "instagram": "https://instagram.com/royalchallengersbangalore",
            "facebook": "https://facebook.com/RoyalChallengersBangalore"
        },
        "achievements": ["IPL Runners-up: 2009, 2011, 2016"],
        "roster": {
            "batsmen": ["Virat Kohli", "Faf du Plessis"],
            "bowlers": ["Mohammed Siraj", "Yash Dayal"],
            "allRounders": ["Glenn Maxwell", "Cameron Green"],
            "wicketkeepers": ["Dinesh Karthik"]
        }
    },
    {
        "id": "kkr",
        "name": "Kolkata Knight Riders",
        "shortName": "KKR",
        "logo": "https://upload.wikimedia.org/wikipedia/en/4/4c/Kolkata_Knight_Riders_Logo.svg",
        "colors": ["#3a225d", "#d4af37"],
        "homeGround": "Eden Gardens, Kolkata",
        "owners": ["Knight Riders Sports Pvt Ltd"],
        "captain": "Shreyas Iyer",
        "headCoach": "Chandrakant Pandit",
        "supportStaff": [{"name": "Abhishek Nayar", "role": "Assistant Coach"}],
        "website": "https://www.kkr.in/",
        "social": {
            "twitter": "https://twitter.com/KKRiders",
            "instagram": "https://instagram.com/kkriders"
        },
        "achievements": ["IPL Champions: 2012, 2014, 2024"],
        "roster": {
            "batsmen": ["Shreyas Iyer", "Rinku Singh"],
            "bowlers": ["Mitchell Starc", "Varun Chakravarthy"],
            "allRounders": ["Sunil Narine", "Andre Russell"],
            "wicketkeepers": ["Rahmanullah Gurbaz"]
        }
    },
    {
        "id": "srh",
        "name": "Sunrisers Hyderabad",
        "shortName": "SRH",
        "logo": "https://upload.wikimedia.org/wikipedia/en/8/81/Sunrisers_Hyderabad.svg",
        "colors": ["#f26a21", "#000000"],
        "homeGround": "Rajiv Gandhi International Cricket Stadium, Hyderabad",
        "owners": ["Sun TV Network"],
        "captain": "Pat Cummins",
        "headCoach": "Daniel Vettori",
        "supportStaff": [{"name": "Muttiah Muralitharan", "role": "Spin Bowling Coach"}],
        "website": "https://www.sunrisershyderabad.in/",
        "social": {
            "twitter": "https://twitter.com/SunRisers",
            "instagram": "https://instagram.com/sunrisershyd"
        },
        "achievements": ["IPL Champions: 2016", "IPL Runners-up: 2018, 2024"],
        "roster": {
            "batsmen": ["Travis Head", "Aiden Markram"],
            "bowlers": ["Bhuvneshwar Kumar", "T Natarajan"],
            "allRounders": ["Abdul Samad"],
            "wicketkeepers": ["Heinrich Klaasen"]
        }
    },
    {
        "id": "rr",
        "name": "Rajasthan Royals",
        "shortName": "RR",
        "logo": "https://upload.wikimedia.org/wikipedia/en/6/60/Rajasthan_Royals_Logo.svg",
        "colors": ["#ea1a85", "#004ba0"],
        "homeGround": "Sawai Mansingh Stadium, Jaipur",
        "owners": ["Royal Multisport Pvt. Ltd"],
        "captain": "Sanju Samson",
        "headCoach": "Kumar Sangakkara (Director of Cricket)",
        "supportStaff": [{"name": "Lasith Malinga", "role": "Fast Bowling Coach"}],
        "website": "https://www.rajasthanroyals.com/",
        "social": {
            "twitter": "https://twitter.com/rajasthanroyals",
            "instagram": "https://instagram.com/rajasthanroyals"
        },
        "achievements": ["IPL Champions: 2008", "Runners-up: 2022"],
        "roster": {
            "batsmen": ["Sanju Samson", "Yashasvi Jaiswal"],
            "bowlers": ["Trent Boult", "Yuzvendra Chahal"],
            "allRounders": ["Riyan Parag"],
            "wicketkeepers": ["Jos Buttler"]
        }
    },
    {
        "id": "dc",
        "name": "Delhi Capitals",
        "shortName": "DC",
        "logo": "https://upload.wikimedia.org/wikipedia/en/2/2f/Delhi_Capitals_Logo.svg",
        "colors": ["#004c93", "#e20613"],
        "homeGround": "Arun Jaitley Stadium, Delhi",
        "owners": ["GMR Group", "JSW Group"],
        "captain": "Rishabh Pant",
        "headCoach": "Ricky Ponting",
        "supportStaff": [{"name": "James Hopes", "role": "Bowling Coach"}],
        "website": "https://www.delhicapitals.in/",
        "social": {
            "twitter": "https://twitter.com/DelhiCapitals",
            "instagram": "https://instagram.com/delhicapitals"
        },
        "achievements": ["IPL Runners-up: 2020"],
        "roster": {
            "batsmen": ["David Warner", "Prithvi Shaw"],
            "bowlers": ["Anrich Nortje", "Kuldeep Yadav"],
            "allRounders": ["Axar Patel"],
            "wicketkeepers": ["Rishabh Pant"]
        }
    },
    {
        "id": "pk",
        "name": "Punjab Kings",
        "shortName": "PBKS",
        "logo": "https://upload.wikimedia.org/wikipedia/en/d/d4/Punjab_Kings_Logo.svg",
        "colors": ["#ed1b24", "#d4af37"],
        "homeGround": "IS Bindra Stadium, Mohali",
        "owners": ["KPH Dream Cricket Pvt Ltd"],
        "captain": "Shikhar Dhawan",
        "headCoach": "Trevor Bayliss",
        "supportStaff": [{"name": "Wasim Jaffer", "role": "Batting Coach"}],
        "website": "https://www.punjabkingsipl.in/",
        "social": {
            "twitter": "https://twitter.com/PunjabKingsIPL",
            "instagram": "https://instagram.com/punjabkingsipl"
        },
        "achievements": ["IPL Runners-up: 2014"],
        "roster": {
            "batsmen": ["Shikhar Dhawan", "Jonny Bairstow"],
            "bowlers": ["Kagiso Rabada", "Arshdeep Singh"],
            "allRounders": ["Sam Curran", "Liam Livingstone"],
            "wicketkeepers": ["Jitesh Sharma"]
        }
    },
    {
        "id": "gt",
        "name": "Gujarat Titans",
        "shortName": "GT",
        "logo": "https://upload.wikimedia.org/wikipedia/en/5/5c/Gujarat_Titans_Logo.svg",
        "colors": ["#1b2133", "#a7a9ac"],
        "homeGround": "Narendra Modi Stadium, Ahmedabad",
        "owners": ["CVC Capital Partners"],
        "captain": "Shubman Gill",
        "headCoach": "Ashish Nehra",
        "supportStaff": [{"name": "Gary Kirsten", "role": "Batting Coach"}],
        "website": "https://www.gujarattitansipl.com/",
        "social": {
            "twitter": "https://twitter.com/gujarat_titans",
            "instagram": "https://instagram.com/gujarat_titans"
        },
        "achievements": ["IPL Champions: 2022", "Runners-up: 2023"],
        "roster": {
            "batsmen": ["Shubman Gill"],
            "bowlers": ["Mohammed Shami", "Rashid Khan"],
            "allRounders": ["Rahul Tewatia"],
            "wicketkeepers": ["Wriddhiman Saha"]
        }
    },
    {
        "id": "lsg",
        "name": "Lucknow Super Giants",
        "shortName": "LSG",
        "logo": "https://upload.wikimedia.org/wikipedia/en/3/3c/Lucknow_Super_Giants_Logo.svg",
        "colors": ["#00b8f1", "#f58220"],
        "homeGround": "BRSABV Ekana Cricket Stadium, Lucknow",
        "owners": ["RPSG Group"],
        "captain": "KL Rahul",
        "headCoach": "Justin Langer",
        "supportStaff": [{"name": "Morne Morkel", "role": "Fast Bowling Coach"}],
        "website": "https://www.lucknowsupergiants.in/",
        "social": {
            "twitter": "https://twitter.com/LucknowIPL",
            "instagram": "https://instagram.com/lucknowsupergiants"
        },
        "achievements": ["Playoffs: 2022, 2023"],
        "roster": {
            "batsmen": ["KL Rahul", "Quinton de Kock"],
            "bowlers": ["Mark Wood", "Ravi Bishnoi"],
            "allRounders": ["Marcus Stoinis", "Krunal Pandya"],
            "wicketkeepers": ["Nicholas Pooran"]
        }
    }
]

# Players master list (flattened from rosters for search/filter). In a complete app, store in DB.
PLAYERS: List[Dict[str, Any]] = []
for t in TEAMS:
    for role_key, role_name in [("batsmen", "Batsman"), ("bowlers", "Bowler"), ("allRounders", "All-rounder"), ("wicketkeepers", "Wicketkeeper")]:
        for p in t.get("roster", {}).get(role_key, []):
            PLAYERS.append({
                "id": f"{t['id']}-{p.lower().replace(' ', '-')}",
                "name": p,
                "nationality": "",  # can be enriched later
                "role": role_name,
                "battingStyle": None,
                "bowlingStyle": None,
                "teamId": t["id"],
                "teamName": t["name"],
                "photo": "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg",
                "iplStats": {"matches": None, "runs": None, "wickets": None, "strikeRate": None}
            })

# Owners data
OWNERS: List[Dict[str, Any]] = []
for t in TEAMS:
    for o in t["owners"]:
        OWNERS.append({
            "id": f"{t['id']}-{o.lower().split()[0]}",
            "name": o,
            "teamId": t["id"],
            "teamName": t["name"],
            "logo": "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg",
            "description": "",
            "history": []
        })

# Staff data
STAFF: List[Dict[str, Any]] = []
for t in TEAMS:
    if t.get("headCoach"):
        STAFF.append({
            "id": f"{t['id']}-headcoach",
            "name": t["headCoach"],
            "role": "Head Coach",
            "teamId": t["id"],
            "teamName": t["name"],
            "photo": "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg",
        })
    for s in t.get("supportStaff", []):
        STAFF.append({
            "id": f"{t['id']}-{s['role'].lower().replace(' ', '-')}",
            "name": s["name"],
            "role": s["role"],
            "teamId": t["id"],
            "teamName": t["name"],
            "photo": "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg",
        })

# ------------------------------------------------------------------
# Base routes
# ------------------------------------------------------------------
@app.get("/")
def read_root():
    return {"message": "IPL Encyclopedia API is running"}

@app.get("/api/hello")
def hello():
    return {"message": "Hello from the backend API!"}

# ------------------------------------------------------------------
# Teams
# ------------------------------------------------------------------
@app.get("/api/teams")
def list_teams():
    return TEAMS

@app.get("/api/teams/{team_id}")
def get_team(team_id: str):
    for t in TEAMS:
        if t["id"] == team_id:
            return t
    raise HTTPException(status_code=404, detail="Team not found")

# ------------------------------------------------------------------
# Players
# ------------------------------------------------------------------
@app.get("/api/players")
def list_players(
    q: Optional[str] = Query(None, description="Search query for player name"),
    team: Optional[str] = Query(None, description="Filter by team id"),
    role: Optional[str] = Query(None, description="Filter by role: Batsman, Bowler, All-rounder, Wicketkeeper"),
    nationality: Optional[str] = Query(None, description="Filter by nationality"),
):
    results = PLAYERS
    if q:
        ql = q.lower()
        results = [p for p in results if ql in p["name"].lower()]
    if team:
        results = [p for p in results if p["teamId"] == team]
    if role:
        results = [p for p in results if p["role"].lower() == role.lower()]
    if nationality:
        results = [p for p in results if (p.get("nationality") or "").lower() == nationality.lower()]
    return results

@app.get("/api/players/{player_id}")
def get_player(player_id: str):
    for p in PLAYERS:
        if p["id"] == player_id:
            return p
    raise HTTPException(status_code=404, detail="Player not found")

# ------------------------------------------------------------------
# Staff
# ------------------------------------------------------------------
@app.get("/api/staff")
def list_staff(team: Optional[str] = None):
    if not team:
        return STAFF
    return [s for s in STAFF if s["teamId"] == team]

# ------------------------------------------------------------------
# Owners
# ------------------------------------------------------------------
@app.get("/api/owners")
def list_owners(team: Optional[str] = None):
    if not team:
        return OWNERS
    return [o for o in OWNERS if o["teamId"] == team]

# ------------------------------------------------------------------
# Stats (sample placeholders)
# ------------------------------------------------------------------
@app.get("/api/stats/top-runs")
def top_runs():
    return [
        {"name": "Virat Kohli", "teamId": "rcb", "runs": 8000},
        {"name": "Rohit Sharma", "teamId": "mi", "runs": 6500},
        {"name": "Shikhar Dhawan", "teamId": "pk", "runs": 6000},
    ]

@app.get("/api/stats/top-wickets")
def top_wickets():
    return [
        {"name": "Yuzvendra Chahal", "teamId": "rr", "wickets": 200},
        {"name": "Jasprit Bumrah", "teamId": "mi", "wickets": 180},
        {"name": "Bhuvneshwar Kumar", "teamId": "srh", "wickets": 170},
    ]

# ------------------------------------------------------------------
# Database test passthrough (existing)
# ------------------------------------------------------------------
@app.get("/test")
def test_database():
    response = {
        "backend": "✅ Running",
        "database": "❌ Not Available",
        "database_url": None,
        "database_name": None,
        "connection_status": "Not Connected",
        "collections": []
    }
    try:
        from database import db
        if db is not None:
            response["database"] = "✅ Available"
            response["database_url"] = "✅ Configured"
            response["database_name"] = db.name if hasattr(db, 'name') else "✅ Connected"
            response["connection_status"] = "Connected"
            try:
                collections = db.list_collection_names()
                response["collections"] = collections[:10]
                response["database"] = "✅ Connected & Working"
            except Exception as e:
                response["database"] = f"⚠️  Connected but Error: {str(e)[:50]}"
        else:
            response["database"] = "⚠️  Available but not initialized"
    except ImportError:
        response["database"] = "❌ Database module not found (run enable-database first)"
    except Exception as e:
        response["database"] = f"❌ Error: {str(e)[:50]}"

    response["database_url"] = "✅ Set" if os.getenv("DATABASE_URL") else "❌ Not Set"
    response["database_name"] = "✅ Set" if os.getenv("DATABASE_NAME") else "❌ Not Set"
    return response


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
