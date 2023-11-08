import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
htmlData = response.text
mySoup = BeautifulSoup(htmlData, "html.parser")

allDivElements = mySoup.findAll(name="div", class_="article-title-description__text")
#
for idx in range(len(allDivElements) - 1, -1, -1):  # reverse for loop
    val = allDivElements[idx]
    movieName = val.find(name="h3", class_="title").getText()
    try:
        with open("movieList.txt", mode="a") as movieFile:
            movieFile.write(f"\n{movieName}")
    except FileNotFoundError:
        with open("movieList.txt", mode="w") as movieFile:
            movieFile.write(f"\n{movieName}")

print("writing to file completed, check the file")
