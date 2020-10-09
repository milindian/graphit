import tkinter as tk
import pandas as pd
import os
import subprocess

def draw(event):
    x, y = event.x, event.y
    if canvas.old_coords:
        x1, y1 = canvas.old_coords
        canvas.create_line(x, y, x1, y1)
    canvas.old_coords = x, y

def draw_line(event):

    if str(event.type) == 'ButtonPress':
        canvas.old_coords = event.x, event.y
        print("clicked at", event.x, event.y)
        df = pd.DataFrame({'X-coordinate': event.x, 'Y-coordinate': event.y}, index=[0])
        df.to_csv('coordinates.csv', mode='a', index=False, header=False),
    elif str(event.type) == 'ButtonRelease':
        x, y = event.x, event.y
        x1, y1 = canvas.old_coords
        canvas.create_line(x, y, x1, y1)

def process():
    root.quit()
    dfx = pd.read_csv('coordinates.csv', header=None)
    dfy = dfx.astype(float)
    dfy.columns = ["X-coordinates", "Y-coordinates"]
    dfy['Y-coordinates']=abs(400-dfy['Y-coordinates'])
    dfz=dfy/400
    dfz['X-coordinates'] = dfz['X-coordinates']*float(e.get())
    dfz['Y-coordinates'] = dfz['Y-coordinates']*float(e2.get())
    dfz.to_csv('coordinates.csv', index=False, header=True),
    subprocess.check_call(['open', 'coordinates.csv'])

def on_entry_click(event):       
    global firstclick

    if firstclick:
        firstclick = False
        e.delete(0, "end") 

def on_entry_click2(event):      
    global firstclick2

    if firstclick2:
        firstclick2 = False
        e2.delete(0, "end")

def reset_coords(event):
    canvas.old_coords = None

def deletefile():
    myLabel = tk.Label(root2, text="Started! Go to plot...", fg="green")
    myLabel.grid(row=25, column=0, pady=10)
    if os.path.exists('coordinates.csv'):
        os.remove('coordinates.csv')
    else:
        print("The file does not exist")
    
    myLabelsw = tk.Label(root, text="(0,0)", fg="green")
    myLabelsw.place(relx=0.0, rely=1.0, anchor='sw')
    
    myLabelnw = tk.Label(root, text="(0,%s)" % e2.get(), fg="green")
    myLabelnw.place(relx=0.0, rely=0.0, anchor='nw')
    
    myLabelse = tk.Label(root, text="(%s,%s)" % (e.get(), e2.get()), fg="green")
    myLabelse.place(relx=1.0, rely=0.0, anchor='ne')
    
    myLabelne = tk.Label(root, text="(%s,0)" % e.get(), fg="green")
    myLabelne.place(relx=1.0, rely=1.0, anchor='se')

firstclick = True
firstclick2 = True

root = tk.Tk()
root.title("4. Click and plot!")
root.geometry("400x400+20+300")

root2 = tk.Tk()
root2.title("Settings")


e = tk.Entry(root2)
e.insert(0, "1. Enter maximum X-value")
e.bind('<FocusIn>', on_entry_click)
e.grid(row=0)

e2 = tk.Entry(root2)
e2.bind('<FocusIn>', on_entry_click2)
e2.insert(2, "2. Enter maximum Y-value")
e2.grid(row=10, column=0, pady=10)

myButton1 = tk.Button(root2, text="3. Click to start plotting", command=deletefile)
myButton1.grid(row=20, column=0, pady=10)

myButton2 = tk.Button(root2, text="5. Done plotting! Go to 'coordinates.csv' file...", command=process, fg="red")
myButton2.grid(row=30, column=0, padx=(20,20), pady=10)


canvas = tk.Canvas(root, width=400, height=400, highlightthickness=10, highlightbackground="gray", bg='white')
canvas.pack()
canvas.old_coords = None

root.bind('<ButtonPress-1>', draw_line)
root.bind('<ButtonRelease-1>', draw_line)

#Don't need this
# root.bind('<B1-Motion>', draw)
# root.bind('<ButtonRelease-1>', reset_coords)

root.mainloop()
