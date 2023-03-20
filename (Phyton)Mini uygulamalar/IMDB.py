# IMDB top 250 listesinin sirasiyla isim ve yili

from bs4 import BeautifulSoup
import requests
import lxml

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
request = requests.get(url)

soup = BeautifulSoup(request.content,"lxml")
print(soup)

top_250 = soup.find("tbody",attrs={"class":"lister-list"}).find_all("tr")

film_sira = 1

for film in top_250:
    adi = film.find("td",attrs={"class":"titleColumn"}).a.text
    yili = film.find("td",attrs={"class":"titleColumn"}).span.text

    print("film adi:",adi)
    print("film yili:",yili)

    print("\n\n")
    film_sira += 1