# list of library imported
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

from imutils.video import VideoStream
from imutils import paths
import imutils

from tkinter import messagebox
from tkinter import *

import face_recognition
import pickle
import cv2

import shutil
import curses
import time
import sys
import os

import RPi.GPIO as GPIO
GPIO.setwarnings(False)

from pygame import mixer
mixer.init()

# GPIO setup and some variables defined

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
 
detector = cv2.CascadeClassifier("/home/pi/Desktop/smile/haarcascade_frontalface_default.xml")
global count
count=0

# classes defined
class SampleApp(Tk):
    
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)        
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)        
        self.frames = {}
        self.title("Indian Visitors")
        for F in (StartPage, PageOne, PageTwo, PageThree, lockpage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        
class StartPage(Frame):    

    def __init__(self, parent, controller):
        
        def shutdown():
            os.system("sudo shutdown -h now")
        
        Frame.__init__(self, parent)
        self.controller = controller
        Label(self, text="\nTHE ONLY IMPOSSIBLE JOURNEY IS, \n\n\t\t THE ONE YOU NEVER BEGIN.\t\n\n", fg="green", justify=CENTER).pack()
        Button(self,text='START',width=20, command=lambda: controller.show_frame("PageOne")).pack()
        Button(self,text='SHUTDOWN',width=20, command=shutdown, fg="red").pack()
        Label(self, text="\nCopyright © 2019 Made by dua team", fg="blue", justify=CENTER).pack(side=BOTTOM)    
        
class PageOne(Frame):
     
    def __init__(self, parent, controller):
        
        def verifyface():   
            global count
            if count==0:
                vs = VideoStream(src=0).start()
                messagebox.showinfo("Information","Look at Camera")
                while True and count!=1:
                    fme = vs.read()
                    orig = fme.copy()
                    fme = imutils.resize(fme, width=500)
                    rects = detector.detectMultiScale(cv2.cvtColor(fme, cv2.COLOR_BGR2GRAY), scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
                    for (x, y, w, h) in rects:
                        cv2.rectangle(fme, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.imshow("Frame", fme)
                    cv2.waitKey(1)
                    if len(rects)==1:
                        p= "/home/pi/Desktop/smile/testing/dua" + ".jpg"
                        cv2.imwrite(p, orig)
                        cv2.destroyAllWindows()
                        vs.stop()
                        data = pickle.loads(open("encodings.pickle", "rb").read())
                        image = cv2.imread("/home/pi/Desktop/smile/testing/dua.jpg")
                        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                        boxes = face_recognition.face_locations(rgb, model="hog")
                        encodings = face_recognition.face_encodings(rgb, boxes)
                        names = []
                        for encoding in encodings:
                            matches = face_recognition.compare_faces(data["encodings"], encoding)
                            if True in matches:
                                mixer.music.load("/home/pi/Desktop/smile/audio/unlock.mp3")
                                mixer.music.play()
                                time.sleep(7.0)
                                count=count+1
                                messagebox.showinfo("Information","Unlocked")
                                """
                                motor.backward()
                                time.sleep(3)
                                motor.stop()
                                """
                                break
                            
                            elif False in matches:
                                mixer.music.load("/home/pi/Desktop/smile/audio/lock.mp3")
                                mixer.music.play()
                                time.sleep(3.0)
                                fromaddr = "siddeshwarchalwa1@gmail.com"
                                toaddr = "@Leme1.sid"
                                msg = MIMEMultipart()
                                msg['From'] = fromaddr
                                msg['To'] = toaddr
                                msg['Subject'] = "Alert Notification"
                                body = "Access Denid!, as unauthorised user"
                                msg.attach(MIMEText(body, 'plain'))
                                filename = "dua.jpg"
                                attachment = open("/home/pi/Desktop/smile/testing/dua.jpg", "rb")
                                p = MIMEBase('application', 'octet-stream')
                                p.set_payload((attachment).read())
                                encoders.encode_base64(p)
                                p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                                msg.attach(p)
                                s = smtplib.SMTP('smtp.gmail.com', 587)
                                s.starttls()
                                s.login(fromaddr, "gmail_password")
                                text = msg.as_string()
                                s.sendmail(fromaddr, toaddr, text)
                                s.quit()
                                break
                            break
                        break
                
            else:
                messagebox.showinfo("Information","first do lock action")
                
        def lockdoor():  
            
            global count
            if count==1:
                #motor.backward()
                #time.sleep(3)
                #motor.stop()
                count=count-1
                messagebox.showinfo("Information","locked")
            else:
                messagebox.showinfo("Information","first do unlock action")
                
        Frame.__init__(self, parent)
        self.controller = controller
        Label(self, text="\nFEATURES\n", fg="green", justify=CENTER).pack()
        Button(self, text="ADD NEW USER",width=20, command=lambda: controller.show_frame("PageTwo")).pack()
        Button(self, text="OPEN BAG",width=20, command=verifyface).pack()
        Button(self, text="LOCK BAG",width=20, command=lockdoor).pack()
        Button(self, text="UNLOCK BY CODE",width=20, command=lambda: controller.show_frame("lockpage")).pack()
        Button(self, text="CONTROL BAG",width=20,command=lambda: controller.show_frame("PageThree")).pack()
        Button(self, text="END",width=20, command=lambda: controller.show_frame("StartPage"), fg="red").pack()
        Label(self, text="\nCopyright © 2019 Made by dua team", fg="blue", justify=CENTER).pack(side=BOTTOM)    
        
class PageTwo(Frame):
        
    def __init__(self, parent, controller):
        
        def showfolder():
            messagebox.showinfo("information","{}".format(os.listdir("/home/pi/Desktop/smile/dataset")))

        def deletefolder():
            data=E1.get()
            E1.delete(0, 'end')
            newpath = r'/home/pi/Desktop/smile/dataset/'+ data
            if data=="":
                messagebox.showinfo("Information","please, Enter ID")
            elif os.path.exists(newpath):
                shutil.rmtree(newpath)

        def trainmodel():
            
            msgbox = messagebox.askquestion("Information","Are you sure! you want to start training", icon="warning")
            
            if msgbox == "yes":
                imagePaths = list(paths.list_images("/home/pi/Desktop/smile/dataset/"))
                knownEncodings = []
                knownNames = []
                for (i, imagePath) in enumerate(imagePaths):
                    name = imagePath.split(os.path.sep)[-2]
                    image = cv2.imread(imagePath)
                    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    boxes = face_recognition.face_locations(rgb,model="cnn")
                    encodings = face_recognition.face_encodings(rgb, boxes)
                    for encoding in encodings:
                        knownEncodings.append(encoding)
                        knownNames.append(name)
                data = {"encodings": knownEncodings, "names": knownNames}
                f = open("encodings.pickle", "wb")
                f.write(pickle.dumps(data))
                f.close()
                messagebox.showinfo("Information","Done Training")
            
        def store():
            data=E1.get()
            E1.delete(0, 'end')
            newpath = r'/home/pi/Desktop/smile/dataset/'+ data
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            if data=="":
                messagebox.showinfo("Information","please, Enter ID")
            else:     
                vs = VideoStream(src=0).start()
                total = 0
                messagebox.showinfo("Information","look at Camera")
                while True:
                    frm = vs.read()
                    orig = frm.copy()
                    frm = imutils.resize(frm, width=400)
                    rects = detector.detectMultiScale(cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY), scaleFactor=1.1,minNeighbors=5, minSize=(20, 20))
                    for (x, y, w, h) in rects:
                        cv2.rectangle(frm, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.imshow("Frame", frm)
                    cv2.waitKey(1)
                    if len(rects) == 1:
                        p = os.path.sep.join([newpath, "{}.png".format(str(total).zfill(5))])
                        cv2.imwrite(p, orig)
                        total= total+1
                        if total == 15:
                            break
                        time.sleep(1)
                cv2.destroyAllWindows()
                vs.stop()
                
        Frame.__init__(self, parent)
        self.controller = controller
        Label(self, text="\nOWNER HANDLING FEATURES\n", fg="green", justify=CENTER).pack()
        Label(self,text="Enter UserID").pack()
        E1 = Entry(self)
        E1.pack()
        Button(self,text='OK',width=17, command=store).pack()
        Button(self,text='TRAIN MODEL',width=17, command=trainmodel).pack()
        Button(self,text='LIST USERS',width=17, command=showfolder).pack()
        Button(self,text='REMOVE USER',width=17, command=deletefolder).pack()
        Button(self, text="BACK",width=17, command=lambda: controller.show_frame("PageOne"), fg="red").pack()
        Label(self, text="\nCopyright © 2019 Made by dua team", fg="blue", justify=CENTER).pack(side=BOTTOM)
    
class PageThree(Frame):    
    
    def __init__(self, parent, controller):
        
        def up():
            GPIO.output(40,False)
            GPIO.output(38,True)
            GPIO.output(36,True)
            GPIO.output(32,False)
        
        def Down():
            GPIO.output(40,True)
            GPIO.output(38,False)
            GPIO.output(36,False)
            GPIO.output(32,True)
        
        def left():
            GPIO.output(40,False)
            GPIO.output(38,True)
            GPIO.output(36,False)
            GPIO.output(32,True)
        
        def Right():
            GPIO.output(40,True)
            GPIO.output(38,False)
            GPIO.output(36,True)
            GPIO.output(32,False)
    
        def Quit():
            GPIO.output(40,False)
            GPIO.output(38,False)
            GPIO.output(36,False)
            GPIO.output(32,False)

        Frame.__init__(self, parent)
        self.controller = controller
        Label(self, text="\nCHOOSE TO MOVE\n", fg="green", justify=CENTER).pack()
        Button(self,text='FORWARD',width=20, command=up).pack()
        Button(self,text='BACKWARD',width=20, command=Down).pack()
        Button(self,text='STOP',width=20, command=Quit, fg="blue").pack()
        Button(self,text='LEFT',width=20, command=left).pack()
        Button(self,text='RIGHT',width=20, command=Right).pack()
        Button(self,text='END',width=20, command=lambda:controller.show_frame("PageOne"), fg="red").pack()
        Label(self, text="\nCopyright © 2019 Made by dua team", fg="blue", justify=CENTER).pack(side=BOTTOM)    

class lockpage(Frame):    

    def __init__(self, parent, controller):

        def check():
            global count
            data1=E2.get()
            E2.delete(0, 'end')
            if data1 == "dua1948":                
                if count==1:
                    messagebox.showinfo("Information","unlocked")
                    count=count-1
                else:
                    messagebox.showinfo("Information","bag was unlocked")
            else:
                messagebox.showinfo("information","Enter proper passcode!")
            
        
        def lockdoor():
            
            global count
            E2.delete(0, 'end')
            if count==0:
                messagebox.showinfo("Information","locked")
                count=count+1
            else: 
                messagebox.showinfo("Information","bag was locked")
        
        Frame.__init__(self, parent)
        self.controller = controller
        Label(self, text="\nLOCK METHOD\n", fg="green", justify=CENTER).pack()
        Label(self,text="Enter passcode").pack()
        E2 = Entry(self)
        E2.pack()
        Button(self,text='OK',width=17, command=check).pack()
        Button(self, text="LOCK BAG",width=17, command=lockdoor).pack()
        Button(self, text="BACK",width=17, command=lambda: controller.show_frame("PageOne"), fg="red").pack()
        Label(self, text="\nCopyright © 2019 Made by dua team", fg="blue", justify=CENTER).pack(side=BOTTOM)    


# main function starts here        
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
    
