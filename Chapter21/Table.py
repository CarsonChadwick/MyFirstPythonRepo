from bs4 import BeautifulSoup
import requests
import pandas as pd

aColumns = []
alEast = []
aTeam = []

oResponse = requests.get("http://www.baseball-reference.com/")

soup = BeautifulSoup(oResponse.text, 'html.parser')

oData = soup.find('table', id='standings_AL')

aHeadChildren = oData.findChildren()

for oChild in aHeadChildren :
    if (oChild.name == "thead") :
        for oCol in oChild :
            if(oCol.name == 'tr') :
                for oRow in oCol :
                    if (oRow.name == "th") :
                        aColumns.append(oRow.text)

    if (oChild.name == "tbody") : 
        iCount = 0
        for oInfo in oChild :
            if(oInfo.name == "tr") :
                if ((iCount >= 1) and (iCount <= 5)) :
                    aTeam = []
                    for oTeamInfo in oInfo :
                        if (oTeamInfo.name == 'th') :
                            for oSplit in oTeamInfo :
                                if (oSplit.name == 'a') :
                                    aTeam.append(oSplit.text)
                        elif (oTeamInfo.name == 'td') :
                                    aTeam.append(oTeamInfo.text)
                    alEast.append(aTeam)
                iCount += 1
df = pd.DataFrame({ 
                    "Team" : [alEast[0][0], alEast[1][0], alEast[2][0], alEast[3][0], alEast[4][0]],
                    aColumns[1] : [alEast[0][1], alEast[1][1], alEast[2][1], alEast[3][1], alEast[4][1]],
                    aColumns[2] : [alEast[0][2], alEast[1][2], alEast[2][2], alEast[3][2], alEast[4][2]]

                    })
html_tags = df.to_html()
new_HTML_file = open("index.html", "w")
new_HTML_file.write(html_tags)
new_HTML_file.close()

