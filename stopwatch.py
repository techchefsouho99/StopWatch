import tkinter as Tkinter
def start(label):
    global running
    running=True
    start['state']='disabled'
root=Tkinter.Tk()
root.title("STOPWATCH")
root.minsize(width=250,height=70)
label=Tkinter.Label(root,text="WELCOME!",fg="black",font="Verdana 30 bold")
label.pack()
start=Tkinter.Button(root,text="START",width="15",command=lambda:start(label))
start.pack()
root.mainloop()