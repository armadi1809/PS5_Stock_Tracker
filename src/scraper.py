import requests, smtplib, ssl, time
from bs4 import BeautifulSoup as bs


port = 465
def sendEmail(): 
    pswd = input("Type in the password of the sender email to start the scrape: ")
    context = ssl.create_default_context()
    receiver = "aziz.rmadi@gmail.com"
    message = """ \
    Subject: PS5 restock. 

    A new PS5 restock has arrived. Check it out before the consoles are gone."""

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server: 
        server.login("ps5pricetracker@gmail.com", pswd)
        server.sendmail("ps5pricetracker@gmail.com", receiver, message)
    
    return 
    


    
URL = "https://restocktracker.io/ps5-console-standard-edition"

def getPage(): 
    return requests.get(URL)

def checkAvailability(page): 
    soup = bs(page.content, "html.parser")
    results = soup.find_all("div", class_="store-table__table__out-of-stock__text")
    for result in results: 
        availability = result.find("span", class_ = "body-3")
        if availability.text.strip() == "Out of stock": 
            sendEmail()
            break

if __name__ == "__main__": 
    while True: 
        page = getPage()
        checkAvailability(page)
        time.sleep(3600)
   