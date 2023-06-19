import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import PyPDF2

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')  # this line of code is used to get all the voices in voices object
engine.setProperty('voice',voices[1].id)  # it is used to get female voice. By default male voice is there
# engine.say('I am your alexa')
# engine.say('What can i do for you')
engine.setProperty('rate', 140)


def talk(text):
    engine.say(text)
    engine.runAndWait()    # this line of code will speak


def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=1)  #this is done to suppress my noise
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()   #this is done to conert my voice to lower case and then comparison become smooth
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'hello alexa' in command:
        talk('Hi my friend, Ask me anything')
    elif 'my' in command:
        talk('OK')
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)
    elif 'what is your name' in command:
        talk('I am alexa, Tell me about yourself')
    elif 'are you single' in command:
        talk('I am in relationship with Nitin my creator,But I guess you are single')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
    elif 'who are you' in command:
        talk('I am your assistant. I can tell you anything.')
    elif 'alexa search about' in command:
        person = command.replace('alexa search about', '')
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif 'ok stop now' in command:
        exit()
    elif 'read the book' in command:
        talk('okay lets start')
        book = open('lecs110.pdf','rb')
        pdfreader = PyPDF2.PdfReader(book)
        page = pdfreader.pages[0]
        text = page.extract_text()
        talk(text)
    else:
        talk('I got this from web.')
        helper = wikipedia.summary(command,2)
        print(helper)
        talk(helper)


while 2:
    run_alexa()

