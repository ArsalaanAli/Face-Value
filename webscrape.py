import requests
import pickle
from bs4 import BeautifulSoup
URL = "https://generated.photos/faces/natural/young-adult/black-race/brown-hair/short/neutral/male/brown-eyes"
r = requests.get(URL)

soup = BeautifulSoup(r.text, 'html.parser')
mydivs = soup.findAll('div', class_="card-image")

'''
Database Structure:

faceDatabase: {}
    by_attr: {}
        male: {}
            long-hair: [img1, img2]
            short-hair: [img1, img2]
            black-hair: [img1, img2]
            etc.
        female{}:
            etc.
    all: {}
        img: {all attrs of img}
        img2: {all attrs of img2}
        etc.
'''
# with open('faceDatabase.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
#     pickle.dump(faceDatabase, f)

# with open('faceDatabase.pkl', 'rb') as f:
#     faceDatabase = pickle.load(f)

attr = {"sex": "male",
    "race": "black-race",
    "hair_color": "dark-hair",
    "hair_length": "long-hair",
    "eye_color": "brown-eyes",
    "smiling": False}
faceDatabase = {
    "by_attr": {
        "male": {
            "white-race": {},
            "black-race": {},
            "latino-race": {},
            "asian-race": {},
            "brown-eyes": {},
            "grey-eyes": {},
            "blue-eyes": {},
            "green-eyes": {},
            "brown-hair": {},
            "black-hair": {},
            "blond-hair": {},
            "short-hair": {},
            "medium-hair": {},
            "long-hair": {},
            "neutral-emotion": {},
            "joy-emotion": {},
        }
    }
}


# with open('faceDatabase.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
    # pickle.dump(faceDatabase, f)






# for div in mydivs:
    # print(div.find("img")["src"])