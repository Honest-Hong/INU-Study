from tkinter import *
from random import shuffle
import requests
import bs4
import webbrowser
import threading
from collections import Counter
from konlpy.tag import Twitter

class Article:
    def __init__(self, title, content, url):
        self.title = title #기사 제목
        self.content = content #기사 내용
        self.url = url #기사 링크

    def __repr__(self):
        return self.title + ',' + ',' + self.url + '\n'

class Finder(threading.Thread):
    def __init__(self, keyword):
        super(Finder, self).__init__()
        self.keyword = keyword
    def run(self):
        allText = ""
        for page in range(1,6):
            url = 'http://www.koreaherald.com/search/?q=' + self.keyword + '&dt=2&nt=1&np=' + str(page) + '&hq='
            soup = bs4.BeautifulSoup(requests.get(url).text, 'html.parser', from_encoding='utf-8')
            container = soup.body.find(id='container')
            dd = container.div.findAll('dd')


            for i in range(10):
                try:
                    aList = dd[i].findAll('a')
                    if len(aList) >= 2:
                        print('제목: ', aList[1].text)
                    else:
                        print('제목: ', aList[0].text)
                    print(aList[0]['href'])
                    soup2 = bs4.BeautifulSoup(requests.get(aList[0]['href']).text, 'html.parser', from_encoding='utf-8')
                    article = soup2.body.find(id='articleText')
                    try:
                        allText += article.text
                        if len(articles) < 10:
                            if len(aList) >= 2:
                                articles.append(Article(aList[1].text, article.text,aList[0]['href']))
                            else:
                                articles.append(Article(aList[0].text, article.text,aList[0]['href']))
                    except:
                        print('사이트가 다름')
                        continue
                except:
                    print('기사 없음')
                    break

        h = Twitter()
        temp = h.nouns(allText)
        nouns = []
        for t in temp:
            if len(t) > 1:
                nouns.append(t)
        count = Counter(nouns)
        result = count.most_common(100)

        wResult = Tk()
        wResult.title('결과 화면')
        wResult.geometry('500x800')
        # 기사 10개 버튼들
        for art in articles:
            button = Button(wResult, text=art.title, command = lambda url=art.url : OpenSite(url))
            button.pack()
        frame = Frame(wResult)
        frame.pack()
        maxCount = result[0][1]
        minCount = result[-1][1]
        shuffle(result)
        for i in range(len(result)):
            diff = result[i][1] - minCount
            ratio = diff / (maxCount - minCount)
            fontSize = 50 * ratio
            if fontSize < minSize:
                fontSize = minSize
                
            lbl = Label(frame, text=result[i][0], font=('굴림', int(fontSize)))
            lbl.pack(side=LEFT)
            if (i+1) % 8 == 0:
                frame = Frame(wResult)
                frame.pack()
        wResult.mainloop()

minSize = 5
articles = []

def OpenSite(url):
    webbrowser.open_new(url)

def Search(keyword):
    finder = Finder(keyword)
    finder.start()

def KeyEvent(event):
    global ent
    Search(ent.get())

window = Tk()
window.title('기사 모음')
window.geometry('300x100')
lbl = Label(window, text='검색 키워드')
ent = Entry(window)
ent.bind('<KeyRelease-Return>', KeyEvent)
btn = Button(window, text='검색 시작', command= lambda : Search(ent.get()))
lbl.pack()
ent.pack()
btn.pack()
window.mainloop()
