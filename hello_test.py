import tkinter as tk
import requests

currentVersion = "v0.2"

import requests
r = requests.get('https://raw.githubusercontent.com/Rifald/sync_git_update/main/version.txt')
data = r.text

if (data == currentVersion):
    check =  "App is up to date!"
else:
    check = "App is not up to date!"


root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def hello ():  
    label1 = tk.Label(root, text= 'Hello World! v1.0 \n' + check, fg='blue', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    
button1 = tk.Button(text='Click Me', command=hello, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()