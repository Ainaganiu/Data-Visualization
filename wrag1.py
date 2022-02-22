import bs4 as BeautifulSoup
import requests
try:
    source = requests.get('https://sports.ndtv.com/english-premier-league/stats/top-goal-scorers-player-statsdetail/')
    source.raise_for_status()
except:
    print('check source')


