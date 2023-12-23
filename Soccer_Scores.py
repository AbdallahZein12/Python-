from requests import get
from pprint import PrettyPrinter
import os
from datetime import datetime
import pytz

BASE_URL = "https://api.football-data.org/v4/matches"
headers = {'X-Auth-Token':os.environ.get("SOCCER_TOKEN")}

printer = PrettyPrinter()
data = get(BASE_URL,headers=headers).json()['matches']
matches = data


def date_converter(date):
    utc_datetime = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    
    utc_timezone = pytz.timezone("UTC")
    utc_datetime = utc_timezone.localize(utc_datetime)
    
    est_timezone = pytz.timezone("US/Eastern")
    est_datetime = utc_datetime.astimezone(est_timezone)
    
    est_datetime = str(est_datetime)
    calendar_date = est_datetime.split(" ")[0]
    est_datetime = est_datetime.split(" ")[1].split("-")[0]
    dt_object = datetime.strptime(est_datetime,"%H:%M:%S")
    est_datetime = dt_object.strftime("%I:%M:%S %p")
    est_datetime = str(est_datetime)
    
    date = calendar_date + " " + est_datetime
    return date


for match in matches:
    competition = match['competition']['name']
    date = date_converter(match['utcDate'])
    hometeam = match['homeTeam']['name']
    awayteam = match['awayTeam']['name']
    htscore_home = match['score']['halfTime']['home']
    htscore_away = match['score']['halfTime']['away']
    ftscore_home = match['score']['fullTime']['home']
    ftscore_away = match['score']['fullTime']['away']
    
    print(f"\n\n_______________________\n\n\n Competition: {competition}  -  Date: {date}  \n\n HomeTeam: {hometeam}  -  AwayTeam: {awayteam} \n\n HalfTime Scores: \n {hometeam}: {htscore_home}  -  {awayteam}: {htscore_away} \n\n FullTime Scores: \n {hometeam}: {ftscore_home}  -  {awayteam}: {ftscore_away}\n")

