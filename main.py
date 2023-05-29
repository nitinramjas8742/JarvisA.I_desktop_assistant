import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')  # this line of code is used to get all the voices in voices object
engine.setProperty('voice',voices[1].id)  # it is used to get female voice. By default male voice is there
# engine.say('I am your alexa')
# engine.say('What can i do for you')


def talk(text):
    engine.say(text)
    engine.runAndWait()    # this line of code will speak


def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=1) # this is done to suppress my noise
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()  #this is done to conert my voice to lower case and then comparison become smooth
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif 'what is your name' in command:
        talk('I am alexa, Tell me about yourself')
    elif 'are you single' in command:
        talk('I am in relationship with Nitin my creator,But I guess you are single')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
    else:
        talk('Please say it again')


    run_alexa()

