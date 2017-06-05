from tkinter import *
from random import shuffle
import requests
import bs4
import threading
import webbrowser
from collections import Counter
from konlpy.tag import Twitter

class Article:
    def __init__(self, title, link):
        self.title = title
        self.link = link

    def open(self):
        webbrowser.open(self.link)

class Finder(threading.Thread):
    def __init__(self, keyword):
        super(self.__class__, self).__init__()
        self.keyword = keyword

    def run(self):
        keyword = self.keyword
        allText = ""
        articles = []
        for page in range(1,6):
            url = 'http://www.koreaherald.com/search/?q=' + keyword + '&dt=2&nt=1&np=' + str(page) + '&hq='
            soup = bs4.BeautifulSoup(requests.get(url).text, 'html.parser', from_encoding='utf-8')
            container = soup.body.find(id='container')
            dd = container.div.findAll('dd')

            for i in range(10):
                try:
                    aList = dd[i].findAll('a')
                    soup2 = bs4.BeautifulSoup(requests.get(aList[0]['href']).text, 'html.parser', from_encoding='utf-8')
                    article = soup2.body.find(id='articleText')
                    try:
                        allText += article.text
                        if len(articles) < 10:
                            if len(aList) >= 2:
                                articles.append(Article(aList[1].text, aList[0]['href']))
                            else:
                                articles.append(Article(aList[0].text, aList[0]['href']))
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
        wResult.geometry('500x700')
        for art in articles:
            btn = Button(wResult, text=art.title, command = lambda a = art : a.open())
            btn.pack()
        frame = Frame(wResult)
        frame.pack()
        maxCount = result[0][1]
        minCount = result[-1][1]
        shuffle(result)
        for i in range(len(result)):
            if keyword == result[i][0]:
                result.pop(i)
                break
        for i in range(len(result)):
            diff = result[i][1] - minCount
            ratio = diff / (maxCount - minCount)
            fontSize = 50 * ratio
            if fontSize < 3:
                fontSize = 3
                
            lbl = Label(frame, text=result[i][0], font=('굴림', int(fontSize)))
            lbl.pack(side=LEFT)
            if (i+1) % 8 == 0:
                frame = Frame(wResult)
                frame.pack()
        wResult.mainloop()

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
