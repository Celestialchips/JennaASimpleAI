import wolframalpha
import wikipedia
import PySimpleGUI as sg
import pyttsx3
# engine properties for TTS
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice', voice.id)
engine.say("Hello, What would you like to know?")
engine.runAndWait()

# Connect to Wolframalpha
client = wolframalpha.Client("AWHKQE-WRGGQLELRR")

# SimpleGui Attributes
sg.theme('DarkBrown')
layout = [sg.Text(), sg.InputText()], [sg.Button('Ok'), sg.Button('Cancel')]
window = sg.Window('Jenna', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        wolfram_res = (next(client.query(values[0]).results).text)
        engine.say("Wolfram says: " + wolfram_res, "Wikipedia says: " + wiki_res)
        sg.popup_non_blocking('Wolfram Result: ' + wolfram_res, 'Wikipedia Result: ' + wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = (next(client.query(values[0]).results).text)
        engine.say("Wolfram says: " + wolfram_res)
        sg.popup_non_blocking('Wolfram Result: ' + wolfram_res)
    except wikipedia.exceptions.PageError:
        wolfram_res = (next(client.query(values[0]).results).text)
        engine.say("Wolfram says: " + wolfram_res)
        sg.popup_non_blocking('Wolfram Result: ' + wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        engine.say("Wikipedia says: " + wiki_res)
        sg.popup_non_blocking('Wikipedia Result: ' + wiki_res)

    engine.runAndWait()

    print(values[0])

window.close()