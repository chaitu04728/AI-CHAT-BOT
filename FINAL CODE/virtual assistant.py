from time import time
from more_itertools import take
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
import subprocess as sp
import wolframalpha
import json
import random
from PIL import Image
import pyautogui
import MyAlarm
import winshell as winshell
from forex_python.converter import CurrencyRates
from speedtest import Speedtest
import pywhatkit
from geopy.geocoders import Nominatim
from geopy import distance


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

paths = {
    'notepad': "C:\\Windows\\notepad.exe",
    'calculator':"C:\\Windows\\System32\\calc.exe"
}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(paths['calculator'])

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_notepad():
    os.startfile(paths['notepad'])


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")

    print("Loading your AI personal assistant Sam")
    speak("I am Sam Sir. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:    
        print("Say that again please...")  
        return "None"
    return query


if __name__=="__main__" :
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India - Happy reading')

        elif 'presidency university' in query:
            news = webbrowser.open_new_tab("https://presidencyuniversity.in/")
            speak('Here is the presidency university home page')

        elif 'play music'in query:
            music_dir = 'D:\wipro\jarvis\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(time)

        elif 'open calculator' in query:
            sp.Popen('C:\\Windows\\System32\\calc.exe')

        elif 'open command prompt' in query or 'open cmd' in query:
            sp.Popen('C:\Windows\System32\cmd.exe')

        elif 'open notepad' in query:
            sp.Popen('C:\\Windows\\notepad.exe')

        elif 'open camera' in query:
            open_camera()

        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by chaitanya")
            print("I was built by chaitanya")

        elif 'empty recycle bin' in query or 'clear recycle bin' in query:
            try:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                print("Recycle Bin is cleaned successfully.")
                speak("Recycle Bin is cleaned successfully.")

            except Exception as e:
                print("Recycle bin is already Empty.")
                speak("Recycle bin is already Empty.")

        elif 'cricket table' in query:
            im = Image.open(r"C:\Users\chaitu\Downloads\1.jpeg")
            im.show()

        elif 'coin game' in query:
            moves=["head", "tails"]   
            cmove=random.choice(moves)
            speak("The computer chose " + cmove)

        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'mute volume' in query:
            pyautogui.press("volumemute")

        elif 'shut down' in query:
            print("Do you want to shutdown you system?")
            speak("Do you want to shutdown you system?")
            cmd = takeCommand()
            if 'no' in cmd:
                continue
            else:
                
                os.system("shutdown /s /t 1")

        elif 'restart' in query:
            print("Do you want to restart your system?")
            speak("Do you want to restart your system?")
            cmd = takeCommand()
            if 'no' in cmd:
                continue
            else:
                
                os.system("shutdown /r /t 1")

        elif 'log out' in query:
            print("Do you want to logout from your system?")
            speak("Do you want to logout from your system?")
            cmd = takeCommand()
            if 'no' in cmd:
                continue
            else:
                os.system("shutdown -l")
        
        elif 'write a note' in query or 'make a note' in query:
            speak("What should I write, sir??")
            note = takeCommand()
            file = open('Note.txt', 'a')
            speak("Should I include the date and time??")
            n_conf = takeCommand()
            if 'yes' in n_conf:
                str_time = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(str_time)
                file.write(" --> ")
                file.write(note)
                speak("Point noted successfully.")
            else:
                file.write("\n")
                file.write(note)
                speak("Point noted successfully.")

        elif 'show me the notes' in query or 'read notes' in query:
            speak("Reading Notes")
            file = open("Note.txt", "r")
            data_note = file.readlines()
            # for points in data_note:
            print(data_note)
            speak(data_note)

        elif 'screenshot' in query:
            myScreenshot=pyautogui.screenshot()
            myScreenshot.save(r'D:\wipro\jarvis\screenshots\1.png')
            speak("Your screenshot is saved")
            print("Your screenshot is saved")

        elif 'date' in query:
            strDate = datetime.datetime.today().strftime('%Y-%m-%d')
            print(strDate)
            speak(f"The date is {strDate}")

        elif 'month' in query or 'month is going' in query:
            def tell_month():
                month = datetime.datetime.now().strftime("%B")
                speak(month)
            tell_month()

        elif 'day' in query or 'day today' in query:
            def tell_day():
                day = datetime.datetime.now().strftime("%A")
                speak(day)
            tell_day()

        elif 'who are you' in query:
            speak("I am P.A. (Python Assistant), developed by chaitanya as a project in their company.")

        elif 'what you do' in query:
            speak("I want to help people to do certain tasks on their single voice commands.")

        elif 'what language you use' in query:
            speak("I am written in Python and I generally speak english.")

        elif 'set alarm' in query:
            speak("Tell me the time to set an Alarm. For example, set an alarm for 11:21 AM")
            a_info = takeCommand()
            a_info = a_info.replace('set an alarm for', '')
            a_info = a_info.replace('.', '')
            a_info = a_info.upper()
            MyAlarm.alarm(a_info)   

        elif 'convert currency' in query:
            try:
                curr_list = {
                    'dollar': 'USD',
                    'rupee': 'INR'
                }

                cur = CurrencyRates()
                # print(cur.get_rate('USD', 'INR'))
                speak('From which currency u want to convert?')
                from_cur = takeCommand()
                src_cur = curr_list[from_cur.lower()]
                speak('To which currency u want to convert?')
                to_cur = takeCommand()
                dest_cur = curr_list[to_cur.lower()]
                speak('Tell me the value of currency u want to convert.')
                val_cur = float(takeCommand())
                # print(val_cur)
                print(cur.convert(src_cur, dest_cur, val_cur))
                speak(cur.convert)
            
            except Exception as e:
                print("Couldn't get what you have said, Can you say it again??")

        elif 'internet speed' in query:
            st = Speedtest()
            print("Wait!! I am checking your Internet Speed...")
            speak("Wait!! I am checking your Internet Speed...")
            dw_speed = st.download()
            up_speed = st.upload()
            dw_speed = dw_speed / 1000000
            up_speed = up_speed / 1000000
            print('Your download speed is', round(dw_speed, 3), 'Mbps')
            print('Your upload speed is', round(up_speed, 3), 'Mbps')
            speak(f'Your download speed is {round(dw_speed, 3)} Mbps')
            speak(f'Your upload speed is {round(up_speed, 3)} Mbps')

        elif "weather" in query:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

        elif 'distance' in query:
            geocoder = Nominatim(user_agent="Singh")
            speak("Tell me the first city name??")
            location1 = takeCommand()
            speak("Tell me the second city name??")
            location2 = takeCommand()

            coordinates1 = geocoder.geocode(location1)
            coordinates2 = geocoder.geocode(location2)

            lat1, long1 = coordinates1.latitude, coordinates1.longitude
            lat2, long2 = coordinates2.latitude, coordinates2.longitude

            place1 = (lat1, long1)
            place2 = (lat2, long2)

            distance_places = distance.distance(place1, place2)

            print(f"The distance between {location1} and {location2} is {distance_places}.")
            speak(f"The distance between {location1} and {location2} is {distance_places}")


        elif 'stock price' in query:
            search_term=query.split("for")[-1]
            url="https://google.com/search?q="+ search_term
            webbrowser.get().open(url)
            speak("Here is what i found for"+ search_term)

        elif 'search' in query:
            search_term=query.split("for")[-1]
            url="https://google.com/search?q="+ search_term
            webbrowser.get().open(url)
            speak("Here is what i found for "+ search_term)

        elif 'email' in query:
            search_term = query.split("for")[-1]
            url="https://mail.google.com/mail/u/0/#inbox"
            webbrowser.get().open(url)
            speak("here you can check your gmail")

        elif 'open chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open amazon' in query:
            webbrowser.open("https://www.amazon.in/")

        elif 'close chrome' in query:
            os.system("TASKKILL /F /IM chrome.exe")

        elif 'close notepad' in query:
            os.system("TASKKILL /F /IM notepad.exe")

        elif "calculate" in query:
            try:
                app_id = "JUGV8R-RXJ4RP7HAG"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)

            except Exception as e:
                print("Couldn't get what you have said, Can you say it again??")

        if "exit" in query or "shut of" in query:
            speak("Ok ,thank you for using this application")
            print("Ok ,thank you for using this application")
            exit()