import requests, smtplib,pandas
from bs4 import BeautifulSoup

amazonEndpoint = "https://www.amazon.in/Reebok-Cypress-Running-Shoes-8-FW0366/dp/B082QJDRZV/"
# https://myhttpheader.com/
# below is to pass as headers, not as parameters, these two are mandatory
myHeaders = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


def sendEmail( currentPrice, itemName="itemName"):
    url = amazonEndpoint
    mycsvData = pandas.read_csv("userToken.csv")
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as myEmailconnection:
        hostEmail = mycsvData.iloc[0]["Host Email ID"]
        hostAppPasswd = mycsvData.iloc[0]["app password"]
        recieverEmail = mycsvData.iloc[0]["reciever Email ID"]
        mailSubject = f"Price Drop Alert - {itemName}"
        mailContent = f"""
Dear Customer,

Price has been dropped for {itemName} below 1300, current price is {currentPrice}

plese find below url for booking:
{url}

Happy shopping!!!
        """
        myEmailconnection.starttls()
        myEmailconnection.login(user=hostEmail,password=hostAppPasswd)
        myEmailconnection.sendmail(from_addr=hostEmail, to_addrs=recieverEmail,
                                       msg=f"Subject:{mailSubject}\n\n{mailContent}")

        print("Mail sent")


def checkPriceTracker(priceValue="0",itemName=""):
    priceValue = float(priceValue)
    if priceValue < 1300:
        sendEmail(currentPrice=priceValue,itemName=itemName)
    else:
        print(f"price is above average, current price: {priceValue}")


# -----------------------------------------
# main program starts from here
try:
    response = requests.get(url=amazonEndpoint, headers=myHeaders)
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    # print(response.content)

    # with open(file="delete.html", mode="w") as myHtml:
    #     myHtml.write(response.text)

    mySoup = BeautifulSoup(response.text, "html.parser")
    getSpan = mySoup.find("span", class_="a-price-whole")
    itemName = mySoup.find(name="span",id="productTitle").getText().strip()
    # itemName = itemName.select_one("#productTitle").getText()
    priceValue = getSpan.getText()
    priceValue = priceValue.split(",")
    priceValue = "".join(priceValue)
    # print(priceValue)
    # print(itemName)
    checkPriceTracker(priceValue=priceValue,itemName=itemName)
