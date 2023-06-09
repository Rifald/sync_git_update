import os
import tkinter as tk
import requests
import git
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
currentVersion = "v0.4"
import requests
r = requests.get('https://raw.githubusercontent.com/Rifald/sync_git_update/main/version.txt')
data = r.text
print(data)

def hello ():  
    label1 = tk.Label(root, text= 'Hello World! v0.4 \n' + check, fg='blue', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)

if (data == currentVersion):
    check =  "App is up to date!"
    root= tk.Tk()

    canvas1 = tk.Canvas(root, width = 300, height = 300)
    canvas1.pack()
        
    button1 = tk.Button(text='Click Me', command=hello, bg='brown',fg='white')
    canvas1.create_window(150, 150, window=button1)

    root.mainloop()
else:
    # Instantiate repo object
    repo = git.Repo(dir_path)
    # pull down 
    repo.remotes.origin.pull()
    
    root= tk.Tk()
    canvas1 = tk.Canvas(root, width = 300, height = 300)
    canvas1.pack()
    label1 = tk.Label(root, text= 'Please restart application', fg='blue', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    root.mainloop()


