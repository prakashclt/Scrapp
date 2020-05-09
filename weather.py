import requests
from bs4 import BeautifulSoup
import wget
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
ap="https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.XpngMMgzZPY"
try:
    page = requests.get(ap)
except requests.exceptions.ConnectionError:
    r.status_code = "Connection refused"
soup = BeautifulSoup(page.content, 'html.parser')
temp=soup.find(id="detailed-forecast-body")#id
temp1=temp.find_all(class_="row row-odd row-forecast")#class
new=temp1.find(class_="col-sm-10 forecast-text")
headlines=[temp1[i].get_text() for i in range(0,7)]

Temp=soup.find(id="current_conditions-summary")
Temp1=soup.find(id="current_conditions_detail")
Temp2=soup.find_all(class_="text-right")
Temp1.get_text()
details=[Temp2[i].get_text() for i in range(0,6)]
