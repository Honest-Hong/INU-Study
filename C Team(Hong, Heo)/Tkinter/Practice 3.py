import tkinter

colorBlue = '#0066cc'
colorWhite = '#ffffff'

window = tkinter.Tk()
window.title('C Team Application')
window.geometry('300x300')
window.wm_iconbitmap('test.ico')
window.configure(background=colorBlue)

lbKeyword = tkinter.Label(window, text='Keyword', bg=colorBlue, fg=colorWhite)
entKeyword = tkinter.Entry(window)
lbSubject = tkinter.Label(window, text='Subject', bg=colorBlue, fg=colorWhite)
entSubject = tkinter.Entry(window)
btn = tkinter.Button(window, text='Search', bg='#0000cc', fg=colorWhite)

lbKeyword.pack()
entKeyword.pack()
lbSubject.pack()
entSubject.pack()
btn.pack()

window.mainloop()
