from Tkinter import *
import numpy as np
from PIL import ImageTk, Image

path = '.\\telos.png'
def initialvalues(e1,e2,e3):
    global Starting_enrage
    global Enrage_Final
    global StreakFinal
    global Values
    Starting_enrage = float(e1.get())
    Enrage_Final = float(e2.get())
    StreakFinal = float(e3.get())
    Values = [Starting_enrage, Enrage_Final, StreakFinal]
    return Values

def probability(Current_enrage,Final_enrage,Streak,Kills):
    Probability = []
    if Kills ==1:
        for k in range (1,Streak+1):
            if Current_enrage >= 100:
                Probability.append(1/(np.floor(10000/(10.0 + 0.25*(Current_enrage + 25) + 3.0*k))))
            elif Current_enrage < 25:
                Probability.append((1/(30*(np.floor(10000/(10.0 + 0.25*(Current_enrage + 25) + 3.0*k))))))
            elif Current_enrage>=25 and Current_enrage <100:
                Probability.append(1/(10*((np.floor(10000/(10.0 + 0.25*(Current_enrage + 25) + 3.0*k))))))
            Current_enrage+=(float((Values[1]-Values[0])/Values[2]))
    else:
        for k in range(1,Kills+1):
            if Current_enrage >= 100:
                Probability.append(1/(np.floor(10000/(10.0 + 0.25*(Current_enrage + 25) + 3.0))))
            elif Current_enrage < 25:
                Probability.append((1/(30*(np.floor(10000/(10.0 + 0.25*(Current_enrage+ 25) + 3.0))))))
            elif Current_enrage>=25 and Current_enrage<100: 
                Probability.append(1/(10*((np.floor(10000/(10.0 + 0.25*(Current_enrage + 25) + 3.0))))))
    return Probability


    
def chance_of_unique (Current_enrage,Final_enrage,Streak,Kills):
    chances = []
    probs = []
    Odds = []
    Streak = int(e3.get())
    Kills = var1.get()
    if Kills ==1:
        for k in range (1,Streak+1):
            probs = probability(float(e1.get()),int(e2.get()),int(e3.get()),var1.get())
            chances.append(1-probs[k-1])
        Odds = 1-(np.prod(chances))
        e6.delete(0,'end')
        e5.delete(0,'end')
        e5.insert(0,float("{0:.5f}".format(Odds)))
        e6.insert(0,float("{0:.5f}".format(probs[Streak-1])))
    else:
        Kills = int(e4.get())
        for k in range (1,Kills+1):
            probs = probability(float(e1.get()),int(e2.get()),int(e3.get()),int(e4.get()))
            chances.append(1-probs[k-1])
        Odds = 1-(np.prod(chances))
        e5.delete(0,'end')
        e6.delete(0,'end')
        e6.insert(0,float("{0:.5f}".format(probs[Streak-1])))
        e5.insert(0,float("{0:.5f}".format(Odds)))

    
def raise_error():
    if int(e1.get())> int(e2.get()) and e2['state']!= DISABLED:
        e5.delete(0,'end')
        e6.delete(0,'end')
        e5.insert(0,"wat?")
        e6.insert(0,"wat?")
        raise Exception("final enr less than initial")
    else:
        e5.delete(0,'end')
        e6.delete(0,'end')
        
    
if __name__ == '__main__':
    master = Tk()
    master.minsize(width=400, height=100)
    master.title('Telos Drop rates')
    
    imgopen = Image.open(path)
    
    resized = imgopen.resize((200, 300),Image.ANTIALIAS)
    
    img = ImageTk.PhotoImage(resized)

    Current_enrage = {}

    panel = Label(master, image = img)

    Label(master, text="Current Enrage: ").grid(row=1)
    Label(master, text="Final Enrage: ").grid(row=2)
    Label(master, text="Streak: ").grid(row=3)
    Label(master, text="Kills: ").grid(row=4)
    Label(master, text="Total probability: ").grid(row=5)
    Label(master, text = "Final Kill probability: ").grid(row=6)

    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry (master)
    e4 = Entry(master)
    e5 = Entry(master)
    e6 = Entry(master)
    
    
    e1.insert(0,"1")
    e2.insert(100,"1")
    e3.insert(1,"1")
    e4.insert(1,"1")
    e5.insert(0,"0")
    e6.insert(0,"0")

    e3.configure(state='disabled')
    e1.configure(state='normal')
    e2.configure(state='disabled')
          
    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=3, column=1)
    e4.grid(row=4, column=1)
    e5.grid(row=5, column=1)
    e6.grid(row=6, column=1)
    panel.grid(row = 0, column = 6, columnspan = 10, rowspan = 16,
               sticky = W+E+N+S, padx = 5, pady = 5)
    

    
    var1 = IntVar()
    def check():
        if var1.get()==1:
            e3.configure(state='normal')
            e4.configure(state='disabled')
            e2.configure(state='normal')
        else:
            e3.configure(state='disabled')
            e4.configure(state='normal')
            e2.configure(state='disabled')
    b0 = Checkbutton(master,text="Streaking?",variable=var1,command=lambda: check()).grid(row=0,column = 1)
    
    b1 = Button(master,text='Chance of Unique',command=lambda: (raise_error(),initialvalues(e1,e2,e3),chance_of_unique(e1,e2,e3,e4))).grid(row=7,column=1)
    

    Button(master, text='Quit', command=master.destroy).grid(row=7, column=0, sticky=W, pady=4)
    mainloop( )


