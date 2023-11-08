from bs4 import BeautifulSoup

with open(file="website.html") as webFile:
    htmldata = webFile.read()
    # print(htmldata)

soup = BeautifulSoup(markup=htmldata, parser="html.parser")

# print(soup.title) # <title>Angela's Personal Site</title>
# print(soup.title.name)  # title
# print(soup.title.string) # Angela's Personal Site

# print(soup) #entire html
# print(soup.prettify()) # read entire html with indentation


allAnchorTags = soup.findAll(name="a")
# print(allAnchorTags)
'''
output for above: 

[<a href="https://www.appbrewery.co/">The App Brewery</a>, 
<a href="https://angelabauer.github.io/cv/hobbies.html">My Hobbies</a>, 
<a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>]
'''

# for tags in allAnchorTags:
#     print(tags.getText())
''' output for above: 

The App Brewery
My Hobbies
Contact Me
'''

# for tags in allAnchorTags:
#     print(tags.get("href"))

''' output for above: 

https://www.appbrewery.co/
https://angelabauer.github.io/cv/hobbies.html
https://angelabauer.github.io/cv/contact-me.html
'''

# heading = soup.find(name="h1", id="name")
# print(heading)  # <h1 id="name">Angela Yu</h1>

# firstClassHeading = soup.find(name="h3", class_="heading")
# print(firstClassHeading) # <h3 class="heading">Books and Teaching</h3>

# getUrl = soup.select_one(selector="p a") # Get everything inside the paragraph and anchor tags
# print(getUrl)

# headingWithClass = soup.select(".heading")
# print(headingWithClass) # [<h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>]

headingWithClass = soup.findAll(name="h3", class_="heading")
print(headingWithClass) # [<h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>]


