import requests
import pickle
from bs4 import BeautifulSoup
URL = "https://generated.photos/faces/natural/young-adult/black-race/black-hair/short/neutral/male/brown-eyes"
r = requests.get(URL)
sex = "male"

attr = {"sex": sex,
    "race": "black-race",
    "hair_color": "dark-hair",
    "hair_length": "short-hair",
    "eye_color": "brown-eyes",
    "expression": "joy"}


soup = BeautifulSoup(r.text, 'html.parser')
mydivs = soup.findAll('div', class_="card-image")

'''
#RESET DATABASE

faceDatabase = {"by_attr": {"male":{}, "female":{}}, "all":{}}

with open('faceDatabase.pkl', 'wb') as f:  # SAVES DATABASE TO DISK
    pickle.dump(faceDatabase, f)
'''




'''
with open('faceDatabase.pkl', 'rb') as f: #LOADS DATABASE FROM DISK
    faceDatabase = pickle.load(f)

def addToDatabase(image):
    for key, value in attr.items():
        if key == "sex":
            continue
        if value in faceDatabase["by_attr"][sex]:
            faceDatabase["by_attr"][sex][value].append(image)
        else:
            faceDatabase["by_attr"][sex][value] = [image]
    faceDatabase["all"][image] = attr
    return




for idx, div in enumerate(mydivs):
    if(idx>30):
        break
    print(idx)
    imageLink = div.find("img")["src"]
    addToDatabase(imageLink)





with open('faceDatabase.pkl', 'wb') as f:  # SAVES DATABASE TO DISK
    pickle.dump(faceDatabase, f)


print("done")
'''

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