import requests
from bs4 import BeautifulSoup

pictures = []
r = requests.get("https://cyclobold.com/")
soup = BeautifulSoup(r.content, "html.parser")
data = soup.prettify()
images = soup.find_all("div", {'class': 'col-md-6 col-lg-3 mb-4'})
for image in images:
    img = image.find("img", {"class": "lazy img-fluid"})
    pictures.append(str(img))
images = open('image.txt', 'w')
for picture in pictures:
    images.write(picture + "\n")
images.close()