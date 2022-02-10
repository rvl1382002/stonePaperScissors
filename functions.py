from tkinter import *
from tkinter import ttk
import random

class player:
    def __init__(self):
        self.name=None
        self.score=0
        self.choice=None #stone=1; paper=2; scissor=3

class selection:
    def stoneP1(self):
        p1.choice=1
        disable(1)
        display_choice_p1(1)
        print(1)

    def paperP1(self):
        p1.choice=2
        disable(1)
        display_choice_p1(2)
        print(2)

    def scissorP1(self):
        p1.choice=3
        disable(1)
        display_choice_p1(3)
        print(3)

    def stoneP2(self):
        p2.choice=1
        disable(2)
        display_choice_p2(1)
        print(4)

    def paperP2(self):
        p2.choice=2
        disable(2)
        display_choice_p2(2)
        print(5)

    def scissorP2(self):
        p2.choice=3
        disable(2)
        display_choice_p2(3)
        print(6)
        
#defining choice
def display_choice_p1(value):
    if(value==1):
        choice_img1=stoneImg
    elif(value==2):
        choice_img1=paperImg
    else:
        choice_img1=scissorImg
    choice_player1.config(image=choice_img1)
    choice_player1.place(anchor=CENTER,relx=0.35,rely=0.5)

def random_animation():
    time=['200','100','175','150','125']
    choice_player1_Ani.after(random.choice(time), random_animation)
    labels=[stoneImg,paperImg,scissorImg]
    image = random.choice(labels)
    choice_player1_Ani.config(image=image)
    
        
def display_choice_p2(value):
    if(value==1):
        choice_img2=stoneImg
    elif(value==2):
        choice_img2=paperImg
    else:
        choice_img2=scissorImg
    choice_player2.config(image=choice_img2)
    choice_player2.place(anchor=CENTER,relx=0.65,rely=0.5)
    
    if(mode_value==1):
        choice_player1_Ani.place_forget()
        labels=[stoneImg,paperImg,scissorImg]
        choice_img1=random.choice(labels)
        choice_player1.config(image=choice_img1)
        choice_player1.place(anchor=CENTER,relx=0.35,rely=0.5)
    
       

def disable(plyr):
    if(plyr==1):
        bL1["state"]=DISABLED
        bL2["state"]=DISABLED
        bL3["state"]=DISABLED
    else:
        bR1["state"]=DISABLED
        bR2["state"]=DISABLED
        bR3["state"]=DISABLED
def enable():
    bL1["state"]=NORMAL
    bL2["state"]=NORMAL
    bL3["state"]=NORMAL
    bR1["state"]=NORMAL
    bR2["state"]=NORMAL
    bR3["state"]=NORMAL

# Window control classes------------------------------------------------------------------------------------------
class sample1:
    def helpClicked(self):
        self.x = 1
        clearWindow1()
        helpWindow()

    def aboutUsClicked(self):
        self.x = 2
        clearWindow1()
        aboutUsWindow()

    def singlePlayerClicked(self):
        global rounds
        global p1,p2
        rounds=0
        self.x = 3
        clearWindow1()
        p1.name="Computer"
        p2.name="Player1"
        WarzoneWindow(1)

    def doublePlayerClicked(self):
        global p1,p2, rounds
        rounds=0
        self.x = 4
        clearWindow1()
        p1.name="Player1"
        p2.name="Player2"
        WarzoneWindow(2)

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
        inputtxt1.place(anchor=CENTER, relx=0.1, rely=0.1)
        headL.place_forget()
        save_button1.place(anchor=CENTER, relx=0.175, rely=0.1)

    def change_name2(self):
        bLE2.place_forget()
        inputtxt2.place(anchor=CENTER, relx=0.9, rely=0.1)
        headR.place_forget()
        save_button2.place(anchor=CENTER, relx=0.825, rely=0.1)

    def save_i1(self):
        player1 = inputtxt1.get(1.0, 3.0)
        headL.config(text=player1)
        inputtxt1.place_forget()
        print(player2)
        headL.place(anchor=CENTER, relx=0.1, rely=0.125)
        save_button1.place_forget()
        bRE1.place(anchor=CENTER, relx=0.175, rely=0.15)

    def save_i2(self):
        player2 = inputtxt2.get(1.0, 3.0)
        headR.config(text=player2)
        inputtxt2.place_forget()
        print(player1)
        headR.place(anchor=CENTER, relx=0.9, rely=0.125)
        save_button2.place_forget()
        bLE2.place(anchor=CENTER, relx=0.825, rely=0.15)


# functions implementations--------------------------------------------------------------------------------------------

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
    cross.place_forget()
    score.place_forget()
    roundCount.place_forget()
    choice_player1.place_forget()
    choice_player2.place_forget()
    choice_player1_Ani.place_forget()
    return 0



# home Window--------------------------------------------------------------------------------------------------------
def homeWindow():
    global helpd, head1, head, singlePlayer, doublePlayer, aboutUs, exitButton
    # labels
    head = Label(root, text="Stone Paper Scissors", width="30", font=("bold", 50))
    head.place(anchor=CENTER, relx=0.5, rely=0.08)
    head1 = Label(root, text="Select the mode", width="25", font=("bold", 30))
    head1.place(anchor=CENTER, relx=0.5, rely=0.2)
    # buttons
    singlePlayer = Button(root, text="Single Player", bg="green", fg="white", height=7, width=30,command=ob1.singlePlayerClicked)
    singlePlayer.place(anchor=CENTER, relx=0.5, rely=0.35)
    doublePlayer = Button(root, text="2-Player", bg="green", fg="white", height=7, width=30,command=ob1.doublePlayerClicked)
    doublePlayer.place(anchor=CENTER, relx=0.5, rely=0.53)
    helpd = Button(root, text="HELP", bg="green", fg="white", height=5, width=25, command=ob1.helpClicked)
    helpd.place(anchor=CENTER, relx=0.9, rely=0.9)
    aboutUs = Button(root, text="ABOUT US", bg="green", fg="white", height=5, width=25, command=ob1.aboutUsClicked)
    aboutUs.place(anchor=CENTER, relx=0.1, rely=0.9)
    # program flow
    root.resizable(0, 0)
    root.mainloop()

# Warzone-------------------------------------------------------------------------------------------------------------------
def WarzoneWindow(mode):
    global headL, headR, bL1, bL2, bL3, bR1, bR2, bR3, bB3, bRE1, bLE2, player1, player2, inputtxt2, inputtxt1, save_button1, save_button2,choice_player1,choice_player2
    global sL, sR, stoneImg, paperImg, scissorImg, cross, score, roundCount,choice_img1,choice_img2,mode_value,choice_player1_Ani
    mode_value=mode

    stoneImg = PhotoImage(file=r'stone.png').subsample(3,3)
    paperImg = PhotoImage(file=r"paper.png").subsample(3,3)
    scissorImg = PhotoImage(file=r"scissors.png").subsample(3,3)

    #roundcount
    currentRound="Round "+str(rounds+1)
    roundCount=Label(root,text=currentRound,width=8,font=("bold",30))
    roundCount.place(anchor=CENTER,relx=0.5,rely=0.2)

    #score:
    score=Label(root, text="Score", width=5, font=("bold",40))
    score.place(anchor=CENTER,relx=0.5, rely=0.05)

    # Player mode
    if (mode == 1):
        player1 = "Computer"
        player2 = "Player1"
    else:
        player1 = "Player1"
        player2 = "Player2"
    # label
    headL = Label(root, text=player1, width="30", font=("bold", 30))
    headL.place(anchor=CENTER, relx=0.1, rely=0.1)
    headR = Label(root, text=player2, width="30", font=("bold", 30))
    headR.place(anchor=CENTER, relx=0.9, rely=0.1)

    # buttons(player1)
    bL1 = Button(root, image=stoneImg, command=s.stoneP1)
    bL1.place(anchor=CENTER, relx=0.1, rely=0.28)

    bL2 = Button(root, image=paperImg, command=s.paperP1)
    bL2.place(anchor=CENTER, relx=0.1, rely=0.46)

    bL3 = Button(root, image=scissorImg, command=s.scissorP1)
    bL3.place(anchor=CENTER, relx=0.1, rely=0.64)

    # buttons(player2)
    bR1 = Button(root, image=stoneImg, command=s.stoneP2)
    bR1.place(anchor=CENTER, relx=0.9, rely=0.28)

    bR2 = Button(root, image=paperImg, command=s.paperP2)
    bR2.place(anchor=CENTER, relx=0.9, rely=0.46)

    bR3 = Button(root, image=scissorImg, command=s.scissorP2)
    bR3.place(anchor=CENTER, relx=0.9, rely=0.64)

    # buttons(edit)
    bRE1 = Button(root, text="✎", width="2", height="1", bg="green", command=ob1.change_name1)
    bRE1.place(anchor=CENTER, relx=0.175, rely=0.15)

    bLE2 = Button(root, text="✎", width="2", height="1", bg="green", command=ob1.change_name2)
    bLE2.place(anchor=CENTER, relx=0.825, rely=0.15)

    # back(button)
    bB3 = Button(root, text="back", width="30", height="3", bg="lightblue", command=ob1.homefromWZ)
    bB3.place(anchor=CENTER, relx=0.5, rely=0.8)
    # input(box)
    inputtxt2 = Text(root, height=1, width=21)
    inputtxt1 = Text(root, height=1, width=21)
    # save(button)
    save_button2 = Button(root, text="\u2713", width="2", height="1", bg="green", command=ob1.save_i2)
    save_button1 = Button(root, text="\u2713", width="2", height="1", bg="green", command=ob1.save_i1)
    # separator
    sL = ttk.Separator(root, orient='vertical')
    sL.place(relx=0.2, rely=0.07, relwidth=0, relheight=1)
    sR = ttk.Separator(root, orient='vertical')
    sR.place(relx=0.8, rely=0.07, relwidth=0, relheight=1)

    #war
    cross=Label(root, text='x', width="1", font=("bold", 50))
    cross.place(anchor=CENTER,relx=0.5,rely=0.5)

    #choice display
    choice_player1=Label(root,image=None)
    choice_player2=Label(root,image=None)
    choice_player1_Ani=Label(root,image=None)

    
    if(mode==1):
        disable(1)
        random_animation()
        choice_player1_Ani.place(anchor=CENTER,relx=0.35,rely=0.5)
        

# help----------------------------------------------------------------------------------------------------------------
def helpWindow():
    global heading, label1, bB1
    # message
    msg = '''1.Each Game will have 5 rounds!\n
    2.Player who wins most of the rounds will be winner\n
    3.How to Play:\n
    select Stone,Paper,Scissor
    a)Stone beats sciessor\n
    b)Scissor beats Paper\n
    c)Paper beats Stone'''
    # label(main)
    heading = Label(root, text="<HELP>", fg="black", font=("bold", 50))
    heading.place(anchor=CENTER, relx=0.5, rely=0.08)
    # label(msg)
    label1 = Label(root, text=msg, fg="black", font=("bold", 15), borderwidth=10, relief=SUNKEN, justify=LEFT)
    label1.place(anchor=CENTER, relx=0.5, rely=0.5)
    # Button
    bB1 = Button(root, text="back", width="30", height="3", bg="lightblue", command=ob1.gotoHomeFromHelp)
    bB1.place(anchor=CENTER, relx=0.1, rely=0.1)


# aboutUs-----------------------------------------------------------------------------------------------------------------
def aboutUsWindow():
    global heading1, label2, bB2
    # message
    msg = "We are anonymous for now"
    # label
    heading1 = Label(root, text="About Us", fg="black", font=("bold", 50))
    heading1.place(anchor=CENTER, relx=0.5, rely=0.08)
    label2 = Label(root, text=msg, fg="black", font=("bold", 15), borderwidth=10, relief=SUNKEN, justify=LEFT)
    label2.place(anchor=CENTER, relx=0.5, rely=0.5)
    # Button
    bB2 = Button(root, text="back", width="30", height="3", bg="lightblue", command=ob1.gotoHomeFromAboutUs)
    bB2.place(anchor=CENTER, relx=0.1, rely=0.1)


global root
root = Tk()

# creating object
ob1 = sample1()
s = selection()
root.title("Stone Paper Scissors")
root.geometry('1300x750')
p1=player()
p2=player()
