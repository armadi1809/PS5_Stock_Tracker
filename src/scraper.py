import requests, smtplib, ssl, time
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
import os


port = 465
def sendEmail(): 
    load_dotenv() 
    pswd = os.environ.get("sender_pwd")
    context = ssl.create_default_context()
    receiver = os.environ.get("receiver_email")
    sender = os.environ.get("sender_email")
    message = """ \
    Subject: PS5 restock. 

    A new PS5 restock has arrived. Check it out before the consoles are gone."""

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server: 
        server.login(sender, pswd)
        server.sendmail(sender, receiver, message)
    
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
   