import tkinter
window = tkinter.Tk()
window.title('C Team Application')
window.geometry('300x300')
window.wm_iconbitmap('test.ico')

lbKeyword = tkinter.Label(window, text='Keyword')
entKeyword = tkinter.Entry(window)
lbSubject = tkinter.Label(window, text='Subject')
entSubject = tkinter.Entry(window)
btn = tkinter.Button(window, text='Search')

lbKeyword.pack()
entKeyword.pack()
lbSubject.pack()
entSubject.pack()
btn.pack()

window.mainloop()
