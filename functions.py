from tkinter import *
from tkinter import ttk

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
    #seperatorL.place_forget()
    #seperatorR.place_forget()
    return 0



ob1=sample1()
def homeWindow():
    global helpd
    global head1
    global head
    global singlePlayer
    global doublePlayer
    global aboutUs
    global exitButton


    head=Label(root, text="Stone Paper Scissors", width="30",font=("bold",50))
    head.place(anchor=CENTER, relx=0.5,rely=0.08)

    head1=Label(root, text="Select the mode", width="25", font=("bold",30))
    head1.place(anchor=CENTER, relx=0.5,rely=0.2)

    singlePlayer=Button(root, text="Single Player",bg="green",fg="white",height=7,width=30, command=ob1.singlePlayerClicked)
    singlePlayer.place(anchor=CENTER, relx=0.5,rely=0.35)

    doublePlayer = Button(root, text="2-Player", bg="green", fg="white", height=7, width=30,command=ob1.doublePlayerClicked)
    doublePlayer.place(anchor=CENTER, relx=0.5, rely=0.53)

    helpd = Button(root, text="HELP", bg="green", fg="white", height=5, width=25, command=ob1.helpClicked)
    helpd.place(anchor=CENTER, relx=0.9, rely=0.9)

    aboutUs = Button(root, text="ABOUT US", bg="green", fg="white", height=5, width=25, command=ob1.aboutUsClicked)
    aboutUs.place(anchor=CENTER, relx=0.1, rely=0.9)

    root.resizable(0,0)
    root.mainloop()


#---------------------------------------------------------------------------------------------------------------------

def WarzoneWindow(mode):
    global headL
    global headR
    global bL1
    global bL2
    global bL3
    global bR1
    global bR3
    global bR2
    global seperatorL
    global seperatorR
    if(mode==1):
        player1="Computer"
        player2="Player1"
    else:
        player1="Player1"
        player2="Player2"
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
    #separator
    separatorL=ttk.Separator(root, orient='vertical')
    separatorL.place(relx=0.2, rely=0.07,relwidth=0,relheight=1)
    separatorR=ttk.Separator(root, orient='vertical')
    separatorR.place(relx=0.8, rely=0.07,relwidth=0,relheight=1)

    global bB3
    bB3=Button(root,text="back",width="30",height="3",bg="lightblue",command=ob1.homefromWZ)
    bB3.place(anchor=CENTER,relx=0.5,rely=0.5)


#help----------------------------------------------------------------------------------------------------------------
def helpWindow():
    global heading
    global label1
    global bB1

    heading=Label(root,text="<HELP>",fg="black",font=("bold",50))
    heading.place(anchor=CENTER, relx=0.5,rely=0.08)

    msg='''1.Each Game will have 5 rounds!\n
    2.Player who wins most of the rounds will be winner\n
    3.How to Play:\n
    select Stone,Paper,Scissor
    a)Stone beats sciessor\n
    b)Scissor beats Paper\n
    c)Paper beats Stone'''

    label1=Label(root, text=msg,fg="black",font=("bold",15),borderwidth=10,relief=SUNKEN,justify=LEFT)
    label1.place(anchor=CENTER, relx=0.5, rely=0.5)

    bB1 = Button(root, text="back", width="30", height="3", bg="lightblue", command=ob1.gotoHomeFromHelp)
    bB1.place(anchor=CENTER, relx=0.1, rely=0.1)


#aboutUs-----------------------------------------------------------------------------------------------------------------
def aboutUsWindow():
    global heading1,label2
    heading1=Label(root,text="About Us",fg="black",font=("bold",50))
    heading1.place(anchor=CENTER, relx=0.5,rely=0.08)

    msg="We are anonymous for now"

    label2=Label(root, text=msg,fg="black",font=("bold",15),borderwidth=10,relief=SUNKEN,justify=LEFT)
    label2.place(anchor=CENTER, relx=0.5, rely=0.5)

    global bB2
    bB2 = Button(root, text="back", width="30", height="3", bg="lightblue", command=ob1.gotoHomeFromAboutUs)
    bB2.place(anchor=CENTER, relx=0.1, rely=0.1)





global root
root = Tk()
root.title("Stone Paper Scissors")
root.geometry('1300x750')
