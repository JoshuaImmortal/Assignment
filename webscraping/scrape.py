import requests
from bs4 import BeautifulSoup
import mysql.connector

r = requests.get("https://cyclobold.com/")
soup = BeautifulSoup(r.content, "html.parser")
data = soup.prettify()
content = soup.find(class_= 'modal-content')
print(content.text)
scrape = open('scrape.pdf', 'w')
scrape.write(content.text)
scrape.close()

# pictures = []
# r = requests.get("https://cyclobold.com/")
# soup = BeautifulSoup(r.content, "html.parser")
# data = soup.prettify()
# images = soup.find_all("div", {'class': 'col-md-6 col-lg-3 mb-4'})
# for image in images:
#     img = image.find("img", {"class": "lazy img-fluid"})
#     pictures.append(str(img))
# images = open('image.txt', 'w')
# for picture in pictures:
#     images.write(picture + "\n")
# images.close()
                                                                                                                     
# db_con = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "",
#     database = "management_db"
# )
# cursor = db_con.cursor()
# r = requests.get("https://cyclobold.com/")
# data = BeautifulSoup(r.content, "html.parser")
# soup = data.prettify()
# ps = data.find_all('p')
# text = ""
# num = 8
# for p in ps:
#     text = p.text
# if cursor:
#     mysql_insert_query = f"""
#                 INSERT INTO `content` VALUES (%s, %s);
# """
#     record = (num, text)
#     cursor.execute(mysql_insert_query, record)
#     db_con.commit()
#     print(text)






