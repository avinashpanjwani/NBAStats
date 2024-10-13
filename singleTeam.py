#Copyright 2023, Avinash Panjwani, All rights reserved.
#This program can take a Statistics Page from ESPN and turn it into a list of players with their stats

from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.espn.com/nba/team/stats/_/name/mia/miami-heat")
soup = BeautifulSoup(page.text, 'html.parser')
#creates file, writes Prettified HTML to file
file = open('myfile.html', 'w')
#looks through html, grabs players to make dictionary of players to positions
rosterCount = 0
teamName = ""

#Finds, prints Team Name
for element in soup.find_all(class_="db pr3 nowrap"):
    teamName += element.text +" "
for element in soup.find_all(class_="db fw-bold"):
    teamName += element.text
print(teamName)

#Finds number of players on the team
for element in soup.find_all(class_="Table__TR Table__TR--sm Table__even"):
    if(element.text == 'Total'):
        break
    rosterCount+=1

#Creates List of Players in Roster
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

#Creates a List of stats to add to each player name
statList = []
for element in soup.find_all(class_="Table__TD"):
    statList.append(element.text)
count = 0
statList = statList[rosterCount+1:13*rosterCount+rosterCount+1]

#Adds stats to players on rosterList
n=0
for element in rosterList:
    element.append(statList[0+13*n:13+13*n])
    n+=1
for player in rosterList:
    print(player)


#barebone for player object
class Player:
    def __init__(player,name, points,assists,rebounds):
        player.name = name
        player.points = points
        player.assists = assists
        player.rebounds = rebounds


