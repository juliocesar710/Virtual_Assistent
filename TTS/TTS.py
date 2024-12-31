import pyttsx3


engine = pyttsx3.init()


texto = "Olá, como você está?"


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  


rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)


engine.say(texto)


engine.runAndWait()
