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


from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt, QThread
from PyQt5.QtGui import QMovie, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
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


    def takecommand(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:



            print("Listening...") 
            r.pause_threshold = 1
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=8)
            except Exception:
                return "none"
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception:
            return "none"
        return query.lower()

    def TaskExecution(self):
        wishMe()
        while True:
            self.query = self.takecommand()

            if self.query == "none":
                continue

            if "hello jarvis" in self.query or "hey jarvis" in self.query:
                speak("hello sir, may i help you with something")

            elif "how are you" in self.query:
                speak("i am fine sir, what about you")
                
            elif "also good" in self.query or "i am fine" in self.query or "i'm fine" in self.query:
                speak("that's great to hear from you.")

            elif "thank you" in self.query or "thanks" in self.query:
                speak("it's my pleasure sir.")
             
            elif "goodbye" in self.query or "offline" in self.query or "exit" in self.query:
                speak("before leaving, i would like to thank you for making me your personal assistant. Thank you very much sir, see you tomorrow, have a nice day, goodbye")
                os._exit(0)

            elif "introduce yourself" in self.query or "who are you" in self.query:
                speak("ok sir, In the year 1943, I was proposed as a model of artificial neurons by Warren McCulloch and Walter Pitts. Later many companies introduced me as Google Assistant, Siri, and Alexa. I think I got my name through the Iron Man movie. I am a voice-based personal assistant where I use different technologies to perform tasks with just one voice command. That's all about me, thank you")        
            
            elif "who am i" in self.query or "do you know me" in self.query:
                speak("Definitely sir, you are Rahul Karmkar. Son of Mr. Basant Karmkar and pursuing your undergraduate degree in Bachelor of Information Technology from Marwari College Ranchi and currently you are living in Tiril Road Kokar Ranchi Jharkhand with your parents")

            elif "let's do some work" in self.query or "let's work" in self.query:
                speak("Okay sir initiating task execution mode. We are all set to perform tasks as per your request. what would you like to perform first?")

            elif 'wikipedia' in self.query:
                speak('searching wikipedia....')
                search_query = self.query.replace("wikipedia","").strip()
                try:
                    results = wikipedia.summary(search_query, sentences=2)
                    speak("According to wikipedia")
                    print(results)
                    speak(results)
                except Exception:
                    speak("Sorry sir, I couldn't find anything on wikipedia regarding that.")

            elif "open paint" in self.query or "draw a mango" in self.query:
                speak("Definitely sir, initiating paint.")
                npath = "C:\\Windows\\system32\\mspaint.exe"
                try:
                    os.startfile(npath)
                except Exception:
                    speak("Sorry sir, I couldn't open paint.")

            elif "close paint" in self.query:
                speak("okay sir closing paint")
                os.system("taskkill /f /im mspaint.exe")

            elif "open notepad" in self.query or "open notebook" in self.query:
                speak("initiating notepad, you can type and save your text there")
                try:
                    npath = "C:\\Windows\\system32\\notepad.exe"
                    os.startfile(npath)
                except Exception:
                    os.system("notepad")
            
            elif "close notepad" in self.query or "close notebook" in self.query:
                speak("okay sir, closing notepad ")
                os.system("taskkill /f /im notepad.exe")

            elif "play music" in self.query or "play song" in self.query:
                speak("Sure sir, playing your favourite song")
                music_dir = r"D:\Rahul\my favourite songs"
                try:
                    if os.path.exists(music_dir):
                        songs = [f for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav', '.m4a'))]
                        if songs:
                            os.startfile(os.path.join(music_dir, songs[0]))
                        else:
                            speak("No songs found in your music directory.")
                    else:
                        speak("Sir, the music directory does not exist.")
                except Exception:
                    speak("Sir, I am unable to access the music directory.")

            elif "open youtube" in self.query:
                speak("opening youtube for you sir")
                if "play" in self.query:
                    song_name = self.query.replace("open youtube", "").replace("and play", "").replace("play", "").strip()
                    if song_name:
                        kit.playonyt(song_name)
                    else:
                        webbrowser.open("www.youtube.com")
                else:
                    webbrowser.open("www.youtube.com")

            elif "open chrome" in self.query or "open browser" in self.query:
                speak("opening browser sir, what should i search?")
                cm = self.takecommand()
                if cm != "none":
                    webbrowser.open(f"https://www.google.com/search?q={cm}")
                else:
                    webbrowser.open("https://www.google.com")
            
            elif "the time" in self.query:
                strTime = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"The time is {strTime}")

            elif "temperature" in self.query:
                try:



                    search = "temperature in ranchi"
                    url = f"https://www.google.com/search?q={search}"
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
                    r = requests.get(url, headers=headers)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp_element = data.find("div", class_="BNeawe")
                    if temp_element:
                        temp = temp_element.text
                        speak(f"Current {search} is {temp}")
                    else:
                        speak("Sir, I couldn't find the temperature information on the page.")
                except Exception as e:
                    print(f"Temperature error: {e}")
                    speak("Sir, I am unable to get the temperature right now.")

            
            elif "open vs code" in self.query or "open visual studio code" in self.query:
                speak("Opening VS Code.")
                path = "C:\\Users\\Pradeep\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                try:
                    os.startfile(path)
                except Exception:
                    speak("Sir, VS Code path is not found.")

            elif "joke" in self.query:
                try:
                    joke = pyjokes.get_joke()
                    print(f"Jarvis: {joke}")
                    clean_joke = joke.replace("'", "").replace('"', '').replace("?", ".").replace("-", " ")
                    speak("Here is a joke for you.")
                    speak(clean_joke)
                except Exception:
                    speak("Sorry sir, I cannot find a joke right now.")

            elif "how to do" in self.query or "activate how to do mode" in self.query:
                speak("How to do mode is Activated, please tell me what you want to know.")
                while True:
                    how = self.takecommand()
                    if "exit" in how or "close" in how or "stop" in how:
                        speak("okay sir, how to do mode is closed")
                        break
                    elif how != "none":
                        try:
                            how_to = search_wikihow(how, 1)
                            if len(how_to) > 0:
                                speak(how_to[0].summary)
                            else:
                                speak("I couldn't find anything on that.")
                        except Exception:
                            speak("Sorry sir, I am not able to find this.")


                   
            


startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
    
    def startTask(self):
        self.movie1 = QtGui.QMovie("gif/212508.gif")




        self.ui.label.setMovie(self.movie1)
        self.movie1.start()
        
        self.movie2 = QtGui.QMovie("gif/00545cb7179c504433d4c8f5e845f286.gif")
        self.ui.label_2.setMovie(self.movie2)
        self.movie2.start()
        
        self.movie3 = QtGui.QMovie("gif/mk7_Diagnostics_BioFeedback_POV.gif")
        self.ui.label_5.setMovie(self.movie3)
        self.movie3.start()

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
