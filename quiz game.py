from tkinter import *
import time
import tkinter as tk
import getpass



    
def c():
    import tkinter.messagebox
    import sys

    q=[
        "1. A self contained bolck of statements that perform a coherent task of some kind is called a?:",
        "2. Recursion is sometimes called?:",
        "3. The directive that can be used to test whether an expression evaluates to a nonzero value or not is?:",
        "4. The number of arguments supplied from the command line,by conversion is known as ?:",
        "5. The expression X=4+2%8 evaluates?:",
        "6. Determind which of the following is valid character constant?",
        "7. Given the statement,maruti.engine.bolts=25.Which of the following is true?",
        "8. To access a structure element using pointer,...........operator is used",
        "9. The ...... operator iis a technique to forcefully convert one data type to the other?",
        "10. Which of the following numerical value is invalid constant?",
    ]

    options=[
        ["Monitor", "Function", "Program", "Structure"],
        ["Circular Defination", "Complex defination", "Procedure", "Union"],
        ["#if","#elif","#endif","#exit"],
        ["arg c","arg v","#define","#include"],
        ["-6","6","4","None"],
        ["//","\0","xyz","052"],
        ["Structure bolts is nested within structure engine","Structure engine is nested within structure maruti","Structure maruti is nested within structure engine","Structure maruti is nested within structure bolts"],
        ["dot(.)","pointer(&)","pointer(*)","arrow(->)"],
        ["Cast","Conversion","Type","Uniary"],
        ["assignment operator","relational operator","logical operator","bitwise shift operator"],
    ]

    a=[2,1,1,1,2,1,2,4,1,4]

    class Quiz:
        def __init__(self,master):
            self.v=IntVar()
            self.qn=0
            self.correct=0
            self.ques=self.createq(master, self.qn)
            self.opts=self.createoptions(master,4)
            self.displayq(self.qn)
            self.lbl=Label(master,text="Check your answer",bd=3,bg='white',anchor=W)
            self.lbl.pack(side=BOTTOM,fill=X,pady=1)
            self.button=Button(master,text="Quit",command=self.quit)
            self.button.pack(side=BOTTOM,pady=1)
            self.button=Button(master,text="Reset",command=self.reset)
            self.button.pack(side=BOTTOM,pady=1)
            self.button=Button(master,text="Next",command=self.next)
            self.button.pack(side=BOTTOM,pady=1)
          
            
        def createq(self, master,qn):
            w=Label(master,text=q[qn])
            w.pack(side=TOP,anchor=W)
            return w

        def createoptions(self,master,n):
            val=0
            b=[]
            while val<n:
                btn=Radiobutton(master,justify=CENTER,variable=self.v,value=val+1)
                b.append(btn)
                btn.pack(side=TOP,anchor=W)
                val=val+1
            return b

        def displayq(self,qn):
            val=0
            self.v.set(0)
            self.ques['text']=q[qn]
            for op in options[qn]:
                self.opts[val]['text']=op
                val=val+1

        def checkq(self,qn):
            #print(self.v.get())
            if self.v.get()==a[qn]:
                return True
            return False


        def printresults(self):
            result="Score"+str(self.correct)+"/"+str(len(q))
            tkinter.messagebox.showinfo("Final score: ",result)
            print("Score: ",self.correct,"/",len(q))

        def quit(self):
            self.lbl['text']='quit'
            print('you quit and your score is:',self.correct)
            tkinter.messagebox.showinfo('you quit and your score is:',self.correct)
            root.destroy()

        def reset(self):
            self.v.set(0)

            
        def next(self):
            if self.checkq(self.qn):
                print(self.qn+1,":Correct")
                self.correct+=1
                print("Your score is: ",self.correct)
                self.lbl['text']="correct+score is",self.correct
                self.lbl.config(bg='light green')
            else:
                print(self.qn+1,":Wrong,And correct answer is:option",a[self.qn])
                print("Your score is: ",self.correct)
                self.lbl['text']='Wrong, option',a[self.qn]
                self.lbl.config(bg='red')
            self.qn=self.qn+1
            print('You have left',len(q)-self.qn,'question(s)')
            if self.qn>=len(q):
                self.printresults()
                if self.correct==len(q):
                    print('congrats.......you correct all the question...........')
                print("GAME OVER..............")
                root.destroy()
            else:
                self.displayq(self.qn)

    def countdown():
        lbl.config(bg='yellow')
        for k in range(60,-1,-1):
            lbl["text"]=k 
            time.sleep(1)
            root.update()
            if k<=10:
                lbl.config(bg='orange')
        lbl.config(bg='red')
        lbl["text"]="Time up"

    root=Tk()
    root.geometry("500x300")
    root.title("C programming")
    label_font=('arial', 40)
    lbl=tk.Label(font=label_font)
    lbl.pack(fill='both')
    app=Quiz(root)
    countdown()
    root.destroy()
    print('TIME UP')
    time.sleep(5)
    root.mainloop()        

def cpp():
    import tkinter.messagebox
    import sys

    q=[
        "1. Which of the following type of class allows only one object of it to be created?",
        "2. Which of the following is not a type of constructor?",
        "3. Which of the following statements is correct?",
        "4. Which of the following is not the member of class?",
        "5. A constructor that accepts __________ parameters is called the default constructor",
        "6. Destructor has the same name as the constructor and it is preceded by ______ .",
        "7. A union that has no constructor can be initialized with another union of __________ type."
    ]

    options=[
        ["Virtual class", "Abstract class", "Singleton class", "Friend class"],
        ["Copy constructor", "Friend constructor", "Default constructor", "Parameterized constructor"],
        ["Base class pointer cannot point to derived class.","Derived class pointer cannot point to base class.","Pointer to derived class cannot be created.","Pointer to base class cannot be created."],
        ["Static function","Friend function","Const function","Virtual function"],
        ["One","Two","No","Three"],
        ["!","?","~","$"],
        ["different","same","virtual","class"]
    ]

    a=[3,2,2,2,3,3,2]

    class Quiz:
        def __init__(self,master):
            self.v=IntVar()
            self.qn=0
            self.correct=0
            self.ques=self.createq(master, self.qn)
            self.opts=self.createoptions(master,4)
            self.displayq(self.qn)
            self.lbl=Label(master,text="Check your answer",bd=3,bg='white',anchor=W)
            self.lbl.pack(side=BOTTOM,fill=X,pady=1)
            self.button=Button(master,text="Quit",command=self.quit)
            self.button.pack(side=BOTTOM,pady=1)
            self.button=Button(master,text="Reset",command=self.reset)
            self.button.pack(side=BOTTOM,pady=1)
            self.button=Button(master,text="Next",command=self.next)
            self.button.pack(side=BOTTOM,pady=1)
          
            
        def createq(self, master,qn):
            w=Label(master,text=q[qn])
            w.pack(side=TOP,anchor=W)
            return w

        def createoptions(self,master,n):
            val=0
            b=[]
            while val<n:
                btn=Radiobutton(master,justify=CENTER,variable=self.v,value=val+1)
                b.append(btn)
                btn.pack(side=TOP,anchor=W)
                val=val+1
            return b

        def displayq(self,qn):
            val=0
            self.v.set(0)
            self.ques['text']=q[qn]
            for op in options[qn]:
                self.opts[val]['text']=op
                val=val+1

        def checkq(self,qn):
            #print(self.v.get())
            if self.v.get()==a[qn]:
                return True
            return False


        def printresults(self):
            result="Score"+str(self.correct)+"/"+str(len(q))
            tkinter.messagebox.showinfo("Final score: ",result)
            print("Score: ",self.correct,"/",len(q))

        def quit(self):
            self.lbl['text']='quit'
            print('you quit and your score is:',self.correct)
            tkinter.messagebox.showinfo('you quit and your score is:',self.correct)
            root.destroy()

        def reset(self):
            self.v.set(0)

            
        def next(self):
            if self.checkq(self.qn):
                print(self.qn+1,":Correct")
                self.correct+=1
                print("Your score is: ",self.correct)
                self.lbl['text']="correct+score is",self.correct
                self.lbl.config(bg='light green')
            else:
                print(self.qn+1,":Wrong,And correct answer is:option",a[self.qn])
                print("Your score is: ",self.correct)
                self.lbl['text']='Wrong, option',a[self.qn]
                self.lbl.config(bg='red')
            self.qn=self.qn+1
            print('You have left',len(q)-self.qn,'question(s)')
            if self.qn>=len(q):
                self.printresults()
                if self.correct==len(q):
                    print('congrats.......you correct all the question...........')
                print("GAME OVER..............")
                root.destroy()
            else:
                self.displayq(self.qn)
                
    def countdown():
        lbl.config(bg='yellow')
        for k in range(60,-1,-1):
            lbl["text"]=k 
            time.sleep(1)
            root.update()
            if k<=10:
                lbl.config(bg='orange')
        lbl.config(bg='red')
        lbl["text"]="Time up"


    root=Tk()
    root.geometry("500x300")
    root.title("CPP programming")
    label_font=('arial', 40)
    lbl=tk.Label(font=label_font)
    lbl.pack(fill='both')
    app=Quiz(root)
    countdown()
    root.destroy()
    print('TIME UP')
    time.sleep(5)
    root.mainloop()        


def quiz():
    import tkinter.messagebox
    import sys

    q=[
        "1. Nobel prize is awarded for which of the following disciplines:",
        "2. Garampani Sanctuary is locate in which of the following places:",
        "3. Entomology studies what?",
        "4. Galileo was an astronomer who",
        "5. Sun exposure can bring about an improvement in health because \nof which of the following reasons:",
        "6. Who is the father of geometry?",
        "7. Who is popularly called as the Iron Man of India?",
        "8. Guru Gopi Krishna is popular for which form of Indian?",
        "9. The radioactive element radium was invented by which of the following scientists?",
        "10. Which of the following items was introduced by James Watt?",
        "11. The most popular invention that is used in our day-to-day life called ballpoint pen was \ninvented by which of the following scientists:",
        "12. Who among the following people received the Bharat Ratna Award \n before becoming the President of India?",
        "13. Kathak is a clasical dance of?",
        "14. The head quarters of Sahitya Academy is at ",
        "15. In which of the following festivals are boat races a special feature"
    ]

    options=[
        ["Literature, peace and economics", "Medicine or Physiology", "Chemistry and Physics", "All the above"],
        ["Junagarh,Gujarat", "Kohima,Nagaland", "Diphu, Assam", "Gangtok, Sikkim"],
        ["Behavior of human beings","Insects","The origin and history of technical and scientific terms","The formation of rocks"],
        ["developed the telescope","discovered four satellites of Jupiter","discovered that the movement of pendulum produces a regular time measurement","All the above."],
        ["the infrared light kills bacteria in the body","resistance power increases","the pigment cells in the skin get stimulated and produce a healthy tan","the ultraviolet rays convert skin oil into Vitamin D"],
        ["Aristotle","Euclid","Kepler","Pythagoras"],
        ["Subhas Chandra Bose","Sardar Vallabhbhai Patel","Jawaharlal Nehru","Govind Ballabh Pant"],
        ["Bharatnatyam","Kuchipudi","Kathak","Manipuri"],
        ["Marie Curie","Benjamin Franklin","Albert Einstein","Issac Newton"],
        ["Hot Air Balloon","Steam Boat","Diving Bell","Rotary Steam Engine"],
        ["Waterman Brothers","Write Brothers","Biro Brothers","Bicc Brothers"],
        ["Dr. Rajendra Prasad","R. Venkatraman","V.V. Giri","Dr. Zakir Hussain"],
        ["Himachal Pradesh","Tamilnadu","Manipur","Kerala"],
        ["Mumbai","Chennai","New Delhi","Kolkata"],
        ["Onam","Bihu","Navratri","Pongal"]
        
    ]

    a=[4,3,2,4,2,2,2,2,1,4,3,4,1,3,1]

    class Quiz:
        def __init__(self,master):
            self.v=IntVar()
            self.qn=0
            self.correct=0
            self.ques=self.createq(master, self.qn)
            self.opts=self.createoptions(master,4)
            self.displayq(self.qn)
            self.lbl=Label(master,text="Check your answer",bd=3,bg='white',anchor=W)
            self.lbl.pack(side=BOTTOM,fill=X,pady=1)
            self.button=Button(master,text="Quit",command=self.quit)
            self.button.pack(side=BOTTOM,pady=1)
            self.button=Button(master,text="Reset",command=self.reset)
            self.button.pack(side=BOTTOM,pady=1)
            self.button=Button(master,text="Next",command=self.next)
            self.button.pack(side=BOTTOM,pady=1)
          
            
        def createq(self, master,qn):
            w=Label(master,text=q[qn])
            w.pack(side=TOP,anchor=W)
            return w

        def createoptions(self,master,n):
            val=0
            b=[]
            while val<n:
                btn=Radiobutton(master,justify=CENTER,variable=self.v,value=val+1)
                b.append(btn)
                btn.pack(side=TOP,anchor=W)
                val=val+1
            return b

        def displayq(self,qn):
            val=0
            self.v.set(0)
            self.ques['text']=q[qn]
            for op in options[qn]:
                self.opts[val]['text']=op
                val=val+1

        def checkq(self,qn):
            #print(self.v.get())
            if self.v.get()==a[qn]:
                return True
            return False


        def printresults(self):
            result="Score"+str(self.correct)+"/"+str(len(q))
            tkinter.messagebox.showinfo("Final score: ",result)
            print("Score: ",self.correct,"/",len(q))

        def quit(self):
            self.lbl['text']='quit'
            print('you quit and your score is:',self.correct)
            tkinter.messagebox.showinfo('you quit and your score is:',self.correct)
            root.destroy()

        def reset(self):
            self.v.set(0)

            
        def next(self):
            if self.checkq(self.qn):
                print(self.qn+1,":Correct")
                self.correct+=1
                print("Your score is: ",self.correct)
                self.lbl['text']="correct+score is",self.correct
                self.lbl.config(bg='light green')
            else:
                print(self.qn+1,":Wrong,And correct answer is:option",a[self.qn])
                print("Your score is: ",self.correct)
                self.lbl['text']='Wrong, option',a[self.qn]
                self.lbl.config(bg='red')
            self.qn=self.qn+1
            print('You have left',len(q)-self.qn,'question(s)')
            if self.qn>=len(q):
                self.printresults()
                if self.correct==len(q):
                    print('congrats.......you correct all the question...........')
                print("GAME OVER..............")
                root.destroy()
            else:
                self.displayq(self.qn)
                
    def countdown():
        lbl.config(bg='yellow')
        for k in range(60,-1,-1):
            lbl["text"]=k 
            time.sleep(1)
            root.update()
            if k<=10:
                lbl.config(bg='orange')
        lbl.config(bg='red')
        lbl["text"]="Time up"


    root=Tk()
    root.geometry("500x300")
    root.title("quiz game")
    label_font=('arial', 40)
    lbl=tk.Label(font=label_font)
    lbl.pack(fill='both')
    app=Quiz(root)
    countdown()
    root.destroy()
    print('TIME UP')
    time.sleep(5)
    root.mainloop()        



print("----------------This is the quiz game---------------------------")
time.sleep(2)
print("Submitted by Dipronil,Pritha,Pradeep,Praggya,Diptamon")
time.sleep(1)
while True:
    u=str(input("Enter user name:"))
    p=str(input("Enter password:"))
    #p=getpass.getpass("Enter password:")
    if(u=="quiz" and p=="1234"):
        print("login sucessfully")
        print("1 for C\n2 for C++\n3 for Quiz game")
        m=eval(input("enter your choice:"))
        print('Your time start now & You have 60 sec')
        time.sleep(1)
        print("---------------------Results---------------------------")
        if m==1:
            c()
        elif m==2:
            cpp()
        elif m==3:
            quiz()
        else:
            print("invalid choice")
    else:
        time.sleep(1)
        print("login failed")
