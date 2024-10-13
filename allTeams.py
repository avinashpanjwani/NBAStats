#This program can traverse the NBA teams page on ESPN to create lists of each teams players and stats

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

driver = webdriver.Edge()
driver.get("https://www.espn.com/nba/teams")
urls = []

for x in range(30):
    elements = driver.find_elements(By.LINK_TEXT,'Statistics')
    elements[x].click()
    urls.append(driver.current_url)
    driver.back()

#file = open('myfile1.html', 'w')

for url in urls:
    #driver.set_window_size(1600,1200)
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    #file = open('myfile1.html','w')
    #file.write(driver.page_source)
    rosterCount = 0
    teamName = ""
    for element in soup.find_all(class_="db pr3 nowrap"):
        teamName += element.text +" "
    for element in soup.find_all(class_="db fw-bold"):
        teamName += element.text
    print(teamName)
    for element in soup.find_all(class_="Table__TR Table__TR--sm Table__even"):
        if(element.text == 'Total'):
            break
        rosterCount+=1
    #Creates a number of players in Roster
    playerString = ""
    rosterList = []
    for element in soup.find_all(class_="Table__TR Table__TR--sm Table__even"):
        temp = []
        if(element.text!='Total'):
            for el in element.text.split(' '):
                if el == "*":
                    break
                else:
                    temp.append(el)
            rosterList.append(temp)
        else:
            break
    #Creates List of Players in Roster
    statList = []
    for element in soup.find_all(class_="Table__TD"):
        statList.append(element.text)
    count = 0
    statList = statList[rosterCount+1:13*rosterCount+rosterCount+1]
    #Creates a List of stats to give to each player
    n=0
    for element in rosterList:
        element.append(statList[0+13*n:13+13*n])
        n+=1
    #print(rosterList)
    #Adds stats to players on rosterList
file = open('myfile1.txt','w')
for player in rosterList:
    file.write(player[0]+' '+player[1] + ','+player[2])
#    for y in range(13):
        
    
class Player:
    def __init__(player,name, points,assists,rebounds):
        player.name = name
        player.points = points
        player.assists = assists
        player.rebounds = rebounds
#barebone for player object
