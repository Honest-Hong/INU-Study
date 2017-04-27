import requests
import bs4

url = 'http://www.uicoop.ac.kr/shop/shop.php?w=3'
soup = bs4.BeautifulSoup(requests.get(url).content, 'html.parser', from_encoding='utf-8')
soup = soup.table.findAll('tr')

def removeBlank(arr):
    ret = []
    for a in arr:
        if a:
            ret.append(a)
    return ret
            
# get dates
td = soup[0].findAll('td')
dates = []
for t in td:
    if t.br:
        dates.append(t.br.text.replace('\t', ''))

# get corner menus
corner = [[[],[],[]] for _ in range(7)]
for numCorner in range(3):
    td = soup[numCorner + 2].findAll('td')
    if numCorner == 0:
        td.pop(0)
    td.pop(0)
    for numDate in range(len(td)):
        text = td[numDate].text.replace('\t', '')
        text = text.replace('\r', '')
        menu = text.split('kcal')
        for m in menu:
            arr = m.split('\n')
            arr = removeBlank(arr)
            if arr:
                arr[-1] = arr[-1] + 'kcal'
                arr[-2] = arr[-2] + '원'
                corner[numDate][numCorner].append(arr)

for i in range(len(dates)):
    print('###', dates[i])
    for j in range(len(corner[i])):
        print(' - 코너', j+1 , '-')
        for c in corner[i][j]:
            text = '('
            for k in range(len(c)):
                if k < len(c) - 2:
                    if k != 0:
                        text += ', '
                    text += c[k]
                    if k == len(c) - 3:
                        text += ') - '
                elif k == len(c) - 2:
                    text += c[k] + ' / '
                else:
                    text += c[k]
                
            print(text)
    print('\n')
