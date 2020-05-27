#This project works for python 3.6 and less

import os 
import time
import speech_recognition as sr 
import pyttsx3
import datetime

# function for greeting
def helloMaster():
    try:
        print('[{}] Thanos: Hello my master!'.format(time))
        engine.say('Hello my master!')
        engine.runAndWait()
    except sr.UnknownValueError:
        print('[{}] Thanos: Sorry but I don\'t understand you'.format(time))
        engine.say('Sorry but I dont understand you')
        engine.runAndWait()

#function for bulling
def bulling():
    try:
        if voice == "Гут аут!":
            print("[{}] Thanos: No! Get out You!\n".format(time))
            engine.say("NO! Get out You!")
            engine.runAndWait()
            smile = open("smile.txt","r")   
            print(smile.read(),"\n")
            smile.close()
        elif voice == "ноу гет фут":
            print("[{}] Thanos: NO! it's get out You!".format(time))
            engine.say("NO! it's get out You!")
            engine.runAndWait()
    except sr.UnknownValueError:
        print('[{}] Thanos: Sorry, but I don\'t understand'.format(time))
        engine.say('Sorry, but I dont understand')
        engine.runAndWait()
# Opens file
def openFile():
    try:
        for x in opt["открой"]:
            if x == voice and x == "яндекс":
                print("Opennig ...")
                return os.startfile('C:/Users/nevermore/AppData/Local/Yandex/YandexBrowser/Application/browser.exe')  
            elif voice == x and (voice == "steam" or voice == "ostin" or voice == "стим"):
                print("Opennig ...")
                return os.startfile('D:\Games\Steam\Steam.exe')
            elif voice == x and voice == "koder":
                print("Opennig ...")
                return os.startfile("D:\Youtube\Microsoft VS Code\Code.exe")
            elif voice == x and (voice == "music" or voice == "музыку"):
                print("Opennig ...")
                return os.startfile("C:\Program Files (x86)\AIMP\AIMP.exe")
            else:
                pass
    except FileNotFoundError:
        print('[{}] Thanos: Sorry but I can not open this file'.format(time))
        engine.say('Sorry but I can not open this file')
        engine.runAndWait()

def silent():
    try:   
        print('[{}] Thanos: Please say something my master'.format(time))
        engine.say('Please say something my master')
        engine.runAndWait()
    except sr.UnknownValueError:
        print('[{}] Thanos: Please say something my master'.format(time))
        engine.say('Please say something my master')
        engine.runAndWait()
# Say time is now
def sayTime():
    try:   
        print('[{0}] Thanos: Time is {0}'.format(time))
        engine.say('Time is {}'.format(time))
        engine.runAndWait()
    except sr.UnknownValueError:
        print('[{}] Thanos: Please say something my master'.format(time))
        engine.say('Please say something my master')
        engine.runAndWait()

def iListen():
    try:   
        print('[{0}] Thanos: Yes my master, I listen!'.format(time))
        engine.say('Yes my master, I listen!')
        engine.runAndWait()
    except sr.UnknownValueError:
        print('[{0}] Thanos: Yes, my master. I listen!'.format(time))
        engine.say('Yes, my master. I listen!')
        engine.runAndWait()

# Looking for a file and open
def lookingForFile():
    f = str(input("Enter name of file: "))
    for address, dirs, files in folder:
        for file in files:
            print(address+'/'+file)
            if file == f:
                return os.startfile(address+"/"+file)
            else: pass

# Looking for a folder and open
def lookingForFolder():
    f = str(input("Enter name of folder: "))
    for address, dirs, files in folder:
        result1 = address.count('/' + f)
        result2 = address.count('\\' + f)
        print(address)
        if result1 == 1:
            return os.startfile(address)
        elif result2 == 1:
            return os.startfile(address)
        else: pass  

# def soundMin():
#     print('[{}] Thanos: Sound is minimal'.format(time))
#     engine.say('Sound is minimal')
#     engine.runAndWait()
#     sound.volume_set(30)

# def soundMax():
#     print('[{}] Thanos: Sound is maximal'.format(time))
#     engine.say('Sound is maximal')
#     engine.runAndWait()
#     sound.volume_max()
# "яндекс","стим",'стэн',"ostin",'steam',"koder","музыку","музон","музыка","music"

opt = {
    "Танос": ('тано',"таносс","тнос","титан"),
    "открой": ("яндекс","стим",'стэн',"ostin",'steam',"koder","музыку","музон","музыка","music")
}

engine = pyttsx3.init()
engine.setProperty('rate', 120)

r = sr.Recognizer()

time = datetime.datetime.today().strftime("%H:%M:%S")

folder = []

helloMaster()

while True:
    try:
        with sr.Microphone(device_index=1) as source:
            print("Say something ...")
            audio = r.listen(source, timeout=1,phrase_time_limit=3)
    except sr.WaitTimeoutError:
            with sr.Microphone(device_index=1) as source:
                print("Say something ...")
                audio = r.listen(source, timeout=1,phrase_time_limit=3)

    try:
        
        voice = r.recognize_google(audio,language="ru-Ru").lower()
        print("You say " + voice)

        if voice == "гет аут":
            bulling()

        elif voice == 'ноу гет аут':
            bulling()

        elif voice == "танос":
            iListen()

        elif voice == "время":
            sayTime()

        elif voice == "открой":
            print('[{}] Thanos: What do you want to open?'.format(time))
            engine.say('What do you want to open?')
            engine.runAndWait()
            print("Say what you whant to open...")
            try:
                with sr.Microphone(device_index=1) as source:
                    audio = r.listen(source, timeout=1,phrase_time_limit=3)
            except sr.WaitTimeoutError:
                pass
            voice = r.recognize_google(audio,language="ru-Ru").lower()
            print("You want to open " + voice)
            openFile()

        elif voice == "поиск":
            print('[{}] Thanos: What are you looking for?'.format(time))
            engine.say('What are you looking for? And could you write this in the comand block?')
            engine.runAndWait()

            w = str(input("What are you looking for? file or folder? "))
            disk = str(input("In what disk (D:/ or C:/) are you looking for {}?: ".format(w)))
            print("Loading...")

            for i in os.walk(disk):
                folder.append(i)
            if w == "file":
                lookingForFile()
            elif w == "folder":
                lookingForFolder()
            else:   
                print("\nPlease repeat the program!")
        
        # elif voice == "минимум звук":
        #     soundMin()
        # elif voice == "максимум звук":
        #     soundMax()
        # else:
        #     print('[{}] Thanos: Sorry but I did click'.format(time))
    except sr.UnknownValueError:
        print('[{}] Thanos: Голос не Розпознано!'.format(time))