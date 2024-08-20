import requests
from bs4 import BeautifulSoup


date = input(" what year you would like to travel to in YYY-MM-DD format")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
yc_web_page = response.text


soup = BeautifulSoup(yc_web_page, "html.parser")
titles = soup.select("li ul li h3")

song_names = [song.getText().strip() for song in titles]
print(song_names)


