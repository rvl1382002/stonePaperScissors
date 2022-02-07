from tkinter import *
from tkinter import ttk

#Window control classes------------------------------------------------------------------------------------------
class sample1:
    def helpClicked(self):
        self.x=1
        clearWindow1()
        helpWindow()
    def aboutUsClicked(self):
        self.x=2
        clearWindow1()
        aboutUsWindow()
    def singlePlayerClicked(self):
        self.x = 3
        clearWindow1()
        WarzoneWindow(1)
    def doublePlayerClicked(self):
        self.x = 4
        clearWindow1()
        WarzoneWindow(2)
    def bL1_try(self):
        x="R1"
    def bL2_try(self):
        x="P1"
    def bL3_try(self):
        x="S1"
    def bR1_try(self):
        x="R2"
    def bR2_try(self):
        x="P2"
    def bR3_try(self):
        x="S2"
    def gotoHomeFromHelp(self):
        clearHelpWindow()
        homeWindow()
    def gotoHomeFromAboutUs(self):
        clearAboutUsWindow()
        homeWindow()
    def homefromWZ(self):
        clearWarzoneWindow()
        homeWindow()
    def change_name1(self):
        bRE1.place_forget()
        inputtxt1.place(anchor=CENTER,relx=0.1,rely=0.1)
        headL.place_forget()
        save_button1.place(anchor=CENTER,relx=0.175,rely=0.1)
        
    def change_name2(self):
        bLE2.place_forget()
        inputtxt2.place(anchor=CENTER,relx=0.9,rely=0.1)
        headR.place_forget()
        save_button2.place(anchor=CENTER,relx=0.825,rely=0.1)        
    def save_i1(self):
        player1=inputtxt1.get(1.0,3.0)
        headL.config(text=player1)
        inputtxt1.place_forget()
        print(player2)
        headL.place(anchor=CENTER,relx=0.1,rely=0.125)
        save_button1.place_forget()
        bRE1.place(anchor=CENTER,relx=0.175,rely=0.1)
    
    def save_i2(self):
        player2=inputtxt2.get(1.0,3.0)
        headR.config(text=player2)
        inputtxt2.place_forget()
        print(player1)
        headR.place(anchor=CENTER,relx=0.9,rely=0.125)
        save_button2.place_forget()
        bLE2.place(anchor=CENTER,relx=0.825,rely=0.1)
    

#functions implementations--------------------------------------------------------------------------------------------
def exit():
    print("Thanks for visiting")
    root.destroy()

def clearWindow1():
    helpd.place_forget()
    doublePlayer.place_forget()
    aboutUs.place_forget()
    singlePlayer.place_forget()
    head.place_forget()
    head1.place_forget()
    return 0

def clearHelpWindow():
    heading.place_forget()
    label1.place_forget()
    bB1.place_forget()
    return 0

def clearAboutUsWindow():
    heading1.place_forget()
    label2.place_forget()
    bB2.place_forget()
    return 0

def clearWarzoneWindow():
    headL.place_forget()
    headR.place_forget()
    bL1.place_forget()
    bL2.place_forget()
    bL3.place_forget()
    bR1.place_forget()
    bR3.place_forget()
    bR2.place_forget()
    bB3.place_forget()
    sL.place_forget()
    sR.place_forget()
    bRE1.place_forget()
    bLE2.place_forget()
    return 0


#creating object
ob1=sample1()


#home Window--------------------------------------------------------------------------------------------------------
def homeWindow():
    global helpd,head1,head,singlePlayer,doublePlayer,aboutUs,exitButton
    #labels
    head=Label(root, text="Stone Paper Scissors", width="30",font=("bold",50))
    head.place(anchor=CENTER, relx=0.5,rely=0.08)
    head1=Label(root, text="Select the mode", width="25", font=("bold",30))
    head1.place(anchor=CENTER, relx=0.5,rely=0.2)
    #buttons
    singlePlayer=Button(root, text="Single Player",bg="green",fg="white",height=7,width=30, command=ob1.singlePlayerClicked)
    singlePlayer.place(anchor=CENTER, relx=0.5,rely=0.35)
    doublePlayer = Button(root, text="2-Player", bg="green", fg="white", height=7, width=30,command=ob1.doublePlayerClicked)
    doublePlayer.place(anchor=CENTER, relx=0.5, rely=0.53)
    helpd = Button(root, text="HELP", bg="green", fg="white", height=5, width=25, command=ob1.helpClicked)
    helpd.place(anchor=CENTER, relx=0.9, rely=0.9)
    aboutUs = Button(root, text="ABOUT US", bg="green", fg="white", height=5, width=25, command=ob1.aboutUsClicked)
    aboutUs.place(anchor=CENTER, relx=0.1, rely=0.9)
    #program flow
    root.resizable(0,0)
    root.mainloop()


#Warzone--------------------------------------------------------------------------------------------------------------------
def WarzoneWindow(mode):
    global headL,headR,bL1,bL2,bL3,bR1,bR2,bR3,sL,sR,bB3,bRE1,bLE2,player1,player2,inputtxt2,inputtxt1,save_button1,save_button2
    #Player mode
    if(mode==1):
        player1="Computer"
        player2="Player1"
    else:
        player1="Player1"
        player2="Player2"
    #label 
    headL=Label(root,text=player1,width="30",font=("bold",30))
    headL.place(anchor=CENTER,relx=0.1,rely=0.1)
    headR=Label(root,text=player2,width="30",font=("bold",30))
    headR.place(anchor=CENTER,relx=0.9,rely=0.1)
    #buttons(left)
    bL1=Button(root,text="Stone",width="30",height="3",bg="lightblue",command=ob1.bL1_try)
    bL1.place(anchor=CENTER,relx=0.1,rely=0.25)
    bL2=Button(root,text="Paper",width="30",height="3",bg="lightblue",command=ob1.bL2_try)
    bL2.place(anchor=CENTER,relx=0.1,rely=0.4)
    bL3=Button(root,text="Scissor",width="30",height="3",bg="lightblue",command=ob1.bL3_try)
    bL3.place(anchor=CENTER,relx=0.1,rely=0.55)
    #buttons(right)
    bR1=Button(root,text="Stone",width="30",height="3",bg="lightblue",command=ob1.bR1_try)
    bR1.place(anchor=CENTER,relx=0.9,rely=0.25)
    bR2=Button(root,text="Paper",width="30",height="3",bg="lightblue",command=ob1.bR2_try)
    bR2.place(anchor=CENTER,relx=0.9,rely=0.4)
    bR3=Button(root,text="Scissor",width="30",height="3",bg="lightblue",command=ob1.bR3_try)
    bR3.place(anchor=CENTER,relx=0.9,rely=0.55)
    #buttons(edit)
    bRE1=Button(root,text="▼",width="2",height="1",bg="green",command=ob1.change_name1)
    bRE1.place(anchor=CENTER,relx=0.175,rely=0.1)
    bLE2=Button(root,text="▼",width="2",height="1",bg="green",command=ob1.change_name2)
    bLE2.place(anchor=CENTER,relx=0.825,rely=0.1)
    #separator
    sL=ttk.Separator(root, orient='vertical')
    sL.place(relx=0.2, rely=0.07,relwidth=0,relheight=1)
    sR=ttk.Separator(root, orient='vertical')
    sR.place(relx=0.8, rely=0.07,relwidth=0,relheight=1)
    #delete(button)
    bB3=Button(root,text="back",width="30",height="3",bg="lightblue",command=ob1.homefromWZ)
    bB3.place(anchor=CENTER,relx=0.5,rely=0.5)
    #input(box)
    inputtxt2= Text(root,height = 1,width = 21)
    inputtxt1= Text(root,height = 1,width = 21)
    #save(button)
    save_button2=Button(root,text="\u2713",width="2",height="1",bg="green",command=ob1.save_i2)
    save_button1=Button(root,text="\u2713",width="2",height="1",bg="green",command=ob1.save_i1)
        

#help----------------------------------------------------------------------------------------------------------------
def helpWindow():
    global heading,label1,bB1
    #message
    msg='''1.Each Game will have 5 rounds!\n
    2.Player who wins most of the rounds will be winner\n
    3.How to Play:\n
    select Stone,Paper,Scissor
    a)Stone beats sciessor\n
    b)Scissor beats Paper\n
    c)Paper beats Stone'''
    #label(main)
    heading=Label(root,text="<HELP>",fg="black",font=("bold",50))
    heading.place(anchor=CENTER, relx=0.5,rely=0.08)
    #label(msg)
    label1=Label(root, text=msg,fg="black",font=("bold",15),borderwidth=10,relief=SUNKEN,justify=LEFT)
    label1.place(anchor=CENTER, relx=0.5, rely=0.5)
    #Button
    bB1 = Button(root, text="back", width="30", height="3", bg="lightblue", command=ob1.gotoHomeFromHelp)
    bB1.place(anchor=CENTER, relx=0.1, rely=0.1)


#aboutUs-----------------------------------------------------------------------------------------------------------------
def aboutUsWindow():
    global heading1,label2,bB2
    #message
    msg="We are anonymous for now"
    #label
    heading1=Label(root,text="About Us",fg="black",font=("bold",50))
    heading1.place(anchor=CENTER, relx=0.5,rely=0.08)
    label2=Label(root, text=msg,fg="black",font=("bold",15),borderwidth=10,relief=SUNKEN,justify=LEFT)
    label2.place(anchor=CENTER, relx=0.5, rely=0.5)
    #Button
    bB2 = Button(root, text="back", width="30", height="3", bg="lightblue", command=ob1.gotoHomeFromAboutUs)
    bB2.place(anchor=CENTER, relx=0.1, rely=0.1)




global root
root = Tk()
root.title("Stone Paper Scissors")
root.geometry('1300x750')
