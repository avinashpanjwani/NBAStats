#Avinash Panjwani 7/20/2023
#This program can take a Statistics Page from ESPN and turn it into a list of players with their stats

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import csv

driver = webdriver.Edge()
driver.get("https://www.espn.com/nba/teams")
filename = "nba_stats.csv"
urls = []
full_stats = []

for x in range(30):
    elements = driver.find_elements(By.LINK_TEXT,'Statistics')
    elements[x].click()
    urls.append(driver.current_url)
    driver.back()

for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')

    rosterCount = 0
    teamName = ""
    for element in soup.find_all(class_="db pr3 nowrap"):
        teamName += element.text +" "
    for element in soup.find_all(class_="db fw-bold"):
        teamName += element.text
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
    for player in rosterList:
        singlePlayerList = []
        singlePlayerList.append(player[0])
        singlePlayerList.append(player[1])
        if(player[2]!='Jr.' and player[2] != 'II' and player[2] != 'III' and player[2] != 'IV' and player[2] != 'Sr.'):
            singlePlayerList.append(player[2])
            for x in range(len(player[3])):
                singlePlayerList.append(player[3][x])
        else:
            singlePlayerList[1] = player[1] + ' ' + player[2]
            singlePlayerList.append(player[3])
            for x in range(len(player[4])):
                singlePlayerList.append(player[4][x])
        full_stats.append(singlePlayerList)
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['First Name','Last Name','Position','GP','GS','MIN','PTS','OR','DR','REB','AST','STL','BLK','TO','PF','AST/TO'])
    csvwriter.writerows(full_stats)
   
        
    

