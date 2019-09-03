from bs4 import BeautifulSoup
import urllib3

csv  = open('result.csv', 'w+')
csv.write('Game ID' + ',' + 'Game Type' + ',' + 'Game Title' + ',' + 'Status' + ',' + 'Updated on' + '\n')

url  = 'https://rpcs3.net/compatibility?p='
http = urllib3.PoolManager()

for i in range(1, 61):

    page = http.request('GET', url+str(i))
    soup = BeautifulSoup(page.data, 'html.parser')

    rows  = soup.findAll('div', {'class':'divTableRow'})

    for row in rows:
        cells      = row.findAll('div', {'class':'divTableCell'})
        cell0      = cells[0]
        cell1      = cells[1]
        cell2      = cells[2]
        cell3      = cells[3]
        gameIDs    = cell0.findAll('a')
        gameTitle  = cell1.text
        gameType   = cell1.a.img['title']
        gameStatus = cell2.div.text
        updateOn   = cell3.text

        for container in gameIDs:
            gameID = container.text
            if len(gameID) != 9:
                continue
            csv.write(gameID + ',' + gameType + ',' + gameTitle + ',' + gameStatus + ',' + updateOn + '\n')

csv.close()
