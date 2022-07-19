# Description
Sony's next gen console has been a rare gem since its release in 2020. Gamers need to be alert in order to get their hands on the beast. </br></br>
This program is a simple web scraper that automatically checks playstation 5 stocks availability (via: ) every hour and notifies the user if an availability is detected. 

# User Guide 
1. Create a gmail address that you want to receive alerts from and gather its App password following this link: https://support.google.com/accounts/answer/185833?hl=en 
2. Clone the code found in this repo. 
3. Create a virtual environment and run: </br>
```
$ pip install -r requirements.txt
```
4. Inside the repo, create a file named ".env" with the following entries: </br>
```
sender_pwd = #App password of sender email
sender_email = #email address of sender
receiver_email = #Your personal email address
``` 
5. Run the script as follows </br>
```
> python scraper.py
```
6. If an availability is found, an email similar to the one seen below will be sent to your personal address set in step 4. </br>
![alt text](/email_example.png) </br>
