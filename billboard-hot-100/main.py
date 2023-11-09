import requests
from bs4 import BeautifulSoup

userDate = input("Which do you want to travel to? type the date in this format: YYYY-MM-DD: ")

billBoardUrl = f"https://www.billboard.com/charts/hot-100/{userDate}/"
response = requests.get(url=billBoardUrl)
response.raise_for_status()
# print(response.text)
mySoup = BeautifulSoup(response.text, "html.parser")

mySoup.find(name="")
allLiTags = mySoup.findAll(name="ul", class_="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max")

# print(len(allLiTags))
for tag in allLiTags:
    songName = tag.select_one("h3").getText().strip()
    artistName = tag.select_one("span").getText().strip()
    print(f"{songName}: {artistName}")


print("program ended")




