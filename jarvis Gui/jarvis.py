import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import requests
from bs4 import BeautifulSoup
import pyjokes
import pywhatkit as kit 
import psutil
import sys
from pywikihow import search_wikihow
import requests

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_jarvisUi



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

# Text to speech...............
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Wish me..............
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Hello sir Good Morning!")

    elif hour>=12 and hour<18:
        speak("Hello sir Good Afternoon!")
        
    else:
        speak("Hello sir Good Evening!")

    speak("I am jarvis. Your personal assistent, plese tell me how may i help you ")

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()



# Take command.................
    def takecommand(self):
        
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...") 
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Reognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            print("Please say that again....")
            return"None"
        return query  

# Task Execution...............
    def TaskExecution(self):
        wishMe()
        while True:
            self.query = self.takecommand().lower()

            
            if "hello jarvis" in self.query or "hey" in self.query:
                speak("hello sir, may i help you with something")

            elif "how are you today" in self.query:
                speak("i am fine sir, what about you")
                
            elif "also good" in self.query or "fine" in self.query:
                speak("that's great to hear from you.")

            elif "thank you" in self.query or "thanks" in self.query:
                speak("it's my pleasure sir.")
             
            elif "goodbye jarvis" in self.query:
                speak("before living, i would like to thank you to make me your personal assistent. Thankyou very much sir, see you tommorow have a nice day goodbye")

            elif "introduce yourself" in self.query:
                speak("ok sir, In the year 1943, i was proposed a model of artifiial neurons by, Warren McCulloch, and Walter pits.Later many companies introduce me as, Google assistent, siri, and  Alexa. I think i got my name through Iron man movie which you are currently using. I am a voice based personal assistent where i uses different technologies to add new unique features. I can automate Task with just one voie command.that's all about me thankyou")        
            
            elif "jarvis do you know about me" in self.query:
                speak("Definitely sir, you are rahul karmkar. Son of mr. Basant karmkar and persuing your undergraduate degree in batchler of information technology from,'Marwari College Ranchi' and currently you are living in,'Tiril Road Kokar Ranchi Jharkhand' with your parents")

            elif "let's do some work" in self.query:
                speak("Okay sir inetiating task execution mode. We are all set to perform task asper your request. what would you like to perform firstli")

            
            elif 'wikipedia' in self.query:
                speak('searching wikipedia....')
                self.query = self.query.replace("wikipedia","")
                results = wikipedia.summary(self.query, sentences=1)
                speak("According to wikipedia")
                print(results)
                speak(results)  


            elif "jarvis can you help me to draw a mango" in self.query:
                speak("Definitely sir, inetiating paint which help you to draw anything.")
                npath = "C:\\Windows\\system32\\mspaint.exe"
                os.startfile(npath)

            elif "close it" in self.query:
                speak("okay sir closing paint")
                os.system("taskkill /f /im mspaint.exe")

            elif "open notepad" in self.query:
                speak("inetiating notepad, you can type and save your text there")
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)
            
            
            elif "close notepad" in self.query:
                speak("okay sir, closing notepad ")
                os.system("taskkill /f /im notepad.exe")


            elif "play music" in self.query:
                speak("Sure sir, playing your all time favourite song")
                music_dir ="D:\Rahul\my favourite songs"
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[0]))

            elif "open youtube and play a video" in self.query:
                speak("opening youtube for you sir")
                webbrowser.open("www.youtube.com")
                kit.playonyt("tokyo drift base booster")

            
            elif "open chrome" in self.query:
                speak("opening chrome sir, but what shouild i search there")
                npath = "C:\\Program Files (x86)\\Internet Explorer\\internet explorer"
                os.startfile(npath)
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")


            
            elif "tell me the time" in self.query or "what's the time jarvis" in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime} or you can see on right top of your screen")


            elif "temperature" in self.query or " tell me the temperature in ranchi." in self.query:
                search = "temperature in ranchi"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text 
                speak(f"current {search} is {temp}, It's quiet a sunny day you can take a ride on your bike")
            
            
            elif "open vs code in new window" in self.query:
                speak("Here new window comes.")
                path = "C:\\Users\\Pradeep\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(path)

            
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "activate how to do mode" in self.query:
                speak("Inetiating, collecting all the possible datas which help you to know any thing")
                while True:
                    speak("How to do mode is Activated,please tell me what you want to know.")
                    how = self.takecommand()
                    try:
                        if "exit" in how or "close it" in how:
                            speak("okay sir, how to do mode is closed")
                            break
                        else:
                            max_results = 1
                            how_to = search_wikihow(how,max_results)
                            assert len (how_to)==1
                            how_to[0].print()
                            speak(how_to[0].summary)
                    
                    except Exception as e:
                        speak("Sorry sir,i am not able to find this") 
                        break
                   
            


startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
    
    def startTask(self):
        self.ui.movie = QtGui.QMovie("gif\\212508.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("gif\\00545cb7179c504433d4c8f5e845f286.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("gif\\mk7_Diagnostics_BioFeedback_POV.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.texttime.setText(label_time)
        self.ui.textdate.setText(label_date)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
