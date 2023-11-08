
from bs4 import BeautifulSoup
import requests
urlEndpoint = "https://news.ycombinator.com/"
response = requests.get(url=urlEndpoint)

mySoup = BeautifulSoup(markup=response.text, parser="html.parser")
rowData = mySoup.findAll(name="tr", class_="athing")
anchorLinkList = []
anchorTextList =[]

for tdData in rowData:
    anchor = tdData.select_one("td span.titleline a")
    anchorLinkList.append(anchor.get("href"))
    anchorTextList.append(anchor.getText())

# upVoteList = []

subRowData = mySoup.findAll(name="td", class_="subtext")
upVoteList = [tdData.select_one(".score").getText() for tdData in subRowData]
# upVoteList = [tdData.select_one("tr td.subtext span.score").getText() for tdData in rowData]
upVoteScore = [int(val.split(" ")[0]) for val in upVoteList]

def getHighScore(anchorTextList=[],anchorLinkList= [], upVoteScore=[]):
    maxScore = max(upVoteScore)
    idxOfMaxScore = upVoteScore.index(maxScore)
    print(f"max Score is: {maxScore}, \nmax score text is : {anchorTextList[idxOfMaxScore]}"
          f"\nmax score link is : {anchorLinkList[idxOfMaxScore]}")

getHighScore(anchorTextList=anchorTextList,anchorLinkList=anchorLinkList, upVoteScore=upVoteScore )
# print(anchorTextList)
# print(upVoteList)
# print(anchorLinkList)
# print(upVoteScore)
# print(max(upVoteScore))







'''
# print(mySoup.title)
tdData = mySoup.find(name="tr", class_= "38180846")
anchorTag= tdData.select_one("td span a")
# print(tdData.select_one("td span a"))
# output for above line
# <a href="https://www.remedygames.com/article/how-northlight-makes-alan-wake-2-shine" rel="noreferrer">Northlight technology in Alan Wake 2</a>

print(anchorTag.getText())
print(anchorTag.get("href"))
upvotes = mySoup.find(name="span",id="score_38180846").getText()
print(upvotes)

'''

