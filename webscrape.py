import requests
import pickle
from bs4 import BeautifulSoup
URL = "https://generated.photos/faces/natural/young-adult/white-race/black-hair/short/neutral/male/brown-eyes"

#SET YOURSELF
#BLOND FEMALE LONG HAIR (SHORT HAIRS LOOK TOO YOUNG) 
#


attr = {"sex": "male",
    "race": "black-race",
    "hair_color": "dark-hair",
    "hair_length": "short-hair",
    "eye_color": "brown-eyes",
    "expression": "neutral"}

eyes = ["blue-eyes", "green-eyes", "brown-eyes", "grey-eyes"]
races = ["black-race", "white-race", "latino-race", "asian-race"]
hairs = ["black-hair", "brown-hair", "blond-hair"]
hairLength = ["long", "medium", "short"]

with open('faceDatabase.pkl', 'rb') as f: #LOADS DATABASE FROM DISK
    faceDatabase = pickle.load(f)

def addFacesFromUrl(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.findAll('div', class_="card-image")

    for idx, div in enumerate(mydivs):
        if(idx>30):
            break
        print(idx)
        imageLink = div.find("img")["src"]
        addToDatabase(imageLink)
    return

def addToDatabase(image):
    if(image in faceDatabase["all"]):
        return
    for key, value in attr.items():
        if key == "sex":
            continue
        if not (value in faceDatabase["by_attr"][sex]):
            faceDatabase["by_attr"][sex][value] = {}
        faceDatabase["by_attr"][sex][value][image] = True
    faceDatabase["all"][image] = attr
    return

with open('faceDatabase.pkl', 'wb') as f:  # SAVES DATABASE TO DISK
    pickle.dump(faceDatabase, f)

print("done")

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

usedAttrs:
black-race
dark-hair
long-hair
brown-eyes
joy
'''
'''
#RESET DATABASE

faceDatabase = {"by_attr": {"male":{}, "female":{}}, "all":{}}

with open('faceDatabase.pkl', 'wb') as f:  # SAVES DATABASE TO DISK
    pickle.dump(faceDatabase, f)
'''