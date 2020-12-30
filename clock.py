import tkinter
from datetime import datetime


root = tkinter.Tk()


def update():
    Time['text'] = f'{datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")}'
    root.after(1, update)


Time = tkinter.Label(root, text='こんにちは', font=('', 30), fg='black')
Time.pack()
update()

root.mainloop()
