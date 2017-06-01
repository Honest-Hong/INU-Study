import tkinter

colorBlue = '#0066cc'
colorWhite = '#ffffff'

window = tkinter.Tk()
window.title('C Team Application')
window.geometry('300x100')
window.wm_iconbitmap('test.ico')
window.configure(background=colorBlue)

def doSearch():
    print('Do search! keyword=%s, subject=%s'%(entKeyword.get(), entSubject.get()))
    entKeyword.delete(0, 'end')

lbKeyword = tkinter.Label(window, text='Keyword', bg=colorBlue, fg=colorWhite)
entKeyword = tkinter.Entry(window)
btn = tkinter.Button(window, text='Search', bg='#0000cc', fg=colorWhite, command=doSearch)

lbKeyword.pack()
entKeyword.pack()
btn.pack()

window.mainloop()
