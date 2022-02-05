from tkinter import *
from tkinter import ttk
global root

root = Tk()
root.title("Stone Paper Scissors")
root.geometry('1300x750')


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
    def doublePlayerClicked(self):
        self.x = 4
        clearWindow1()
        WarzoneWindow()
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
    def gotoHomeFromWarzone(self):
        clearWarzoneWindow()
        homeWindow()

        
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
    headingH.place_forget()
    label1H.place_forget()
    bBH.place_forget()
    return 0
def clearAboutUsWindow():
    heading1A.place_forget()
    label2A.place_forget()
    backButtonA.place_forget()
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
    sL.place_forget()
    sR.place_forget()
    bRB.place_forget()
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

    
#Warzone------------------------------------------------------------------------------------------------------------
def WarzoneWindow():
    global headL,headR,bL1,bL2,bL3,bR1,bR2,bR3,sL,sR,bRB
    print("Warzone called")
    #labels
    headL=Label(root,text="Player 1",width="30",font=("bold",30))
    headL.place(anchor=CENTER,relx=0.1,rely=0.1)
    headR=Label(root,text="Player 2",width="30",font=("bold",30))
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
    sL=ttk.Separator(root, orient='vertical')
    sL.place(relx=0.2, rely=0.07,relwidth=0,relheight=1)
    sR=ttk.Separator(root, orient='vertical')
    sR.place(relx=0.8, rely=0.07,relwidth=0,relheight=1)
    #delete(window)
    bRB=Button(root,text="Back",width="30",height="3",bg="green",command=ob1.gotoHomeFromWarzone)
    bRB.place(anchor=CENTER,relx=0.9,rely=0.9)


#help----------------------------------------------------------------------------------------------------------------
def helpWindow():
    global headingH,label1H,bBH
    #message
    msg='''1.Each Game will have 5 rounds!\n
    2.Player who wins most of the rounds will be winner\n
    3.How to Play:\n
    select Stone,Paper,Scissor
    a)Stone beats sciessor\n
    b)Scissor beats Paper\n
    c)Paper beats Stone'''
    #label(main)
    headingH=Label(root,text="<HELP>",fg="black",font=("bold",50))
    headingH.place(anchor=CENTER, relx=0.5,rely=0.08)
    #label(msg)
    label1H=Label(root, text=msg,fg="black",font=("bold",15),borderwidth=10,relief=SUNKEN,justify=LEFT)
    label1H.place(anchor=CENTER, relx=0.5, rely=0.5)
    #Button
    bBH=Button(root,text="Back",fg="red",width="30",height="3",command=ob1.gotoHomeFromHelp,bg="green")
    bBH.place(anchor=CENTER, relx=0.1, rely=0.1)


#aboutUs-----------------------------------------------------------------------------------------------------------------
def aboutUsWindow():
    global heading1A,label2A,backButtonA
    #message
    msg="We are anonymous for now"
    #label
    heading1A=Label(root,text="About Us",fg="black",font=("bold",50))
    heading1A.place(anchor=CENTER, relx=0.5,rely=0.08)
    label2A=Label(root, text=msg,fg="black",font=("bold",15),borderwidth=10,relief=SUNKEN,justify=LEFT)
    label2A.place(anchor=CENTER, relx=0.5, rely=0.5)
    #Button
    backButtonA=Button(root,text="Back",fg="red",width="30",height="3",command=ob1.gotoHomeFromAboutUs,bg="green")
    backButtonA.place(anchor=CENTER, relx=0.1, rely=0.1)







