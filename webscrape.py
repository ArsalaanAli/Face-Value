import requests
import pickle
from bs4 import BeautifulSoup
URL = "https://generated.photos/faces/natural/young-adult/black-race/brown-hair/short/neutral/male/brown-eyes"
r = requests.get(URL)

soup = BeautifulSoup(r.text, 'html.parser')
mydivs = soup.findAll('div', class_="card-image")

attr = {"sex": "male",
    "race": "race_black",
    "hair_color": "hair_dark",
    "hair_length": "hair_length_long",
    "eye_color": "brown",
    "smiling": False}

with open('objs.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
    x = pickle.load(f)
print(x)
# for div in mydivs:
    # print(div.find("img")["src"])