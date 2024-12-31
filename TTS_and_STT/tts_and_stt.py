import speech_recognition as sr
import pyttsx3
import webbrowser

# Inicializa o motor de TTS (Text-to-Speech)
engine = pyttsx3.init()

# Função para falar o texto
def falar(texto):
    engine.say(texto)
    engine.runAndWait()

# Inicializa o reconhecedor de fala
recognizer = sr.Recognizer()

# Função para ouvir e processar o áudio
def ouvir_comando():
    with sr.Microphone() as source:
        print("Ajustando o ruído ambiente...")
        recognizer.adjust_for_ambient_noise(source)
        print("Por favor, fale algo:")
        
        # Captura o áudio
        audio = recognizer.listen(source)

    try:
        # Reconhece o áudio usando o Google Web Speech API
        texto = recognizer.recognize_google(audio, language="pt-BR")  # Para português brasileiro
        print("Você disse: " + texto)
        return texto.lower()  # Retorna o texto em minúsculas
    except sr.UnknownValueError:
        print("Desculpe, não consegui entender o que você disse.")
        return None
    except sr.RequestError:
        print("Não foi possível conectar ao serviço de reconhecimento de fala.")
        return None

# Loop para continuar ouvindo até a palavra "fechar"
while True:
    comando = ouvir_comando()

    if comando:
        # Verifica os comandos de voz
        if "fechar" in comando:
            print("Programa encerrado.")
            falar("Programa encerrado.")
            break  # Encerra o loop se "fechar" for dito

        elif "vídeo" in comando:
            print("Abrindo o YouTube...")
            falar("Abrindo o YouTube.")
            webbrowser.open("https://www.youtube.com")  # Abre o YouTube

        elif "wiki" in comando:
            print("Abrindo a Wikipedia...")
            falar("Abrindo a Wikipedia.")
            webbrowser.open("https://www.wikipedia.org")  # Abre a Wikipedia

        elif "mapa" in comando:
            print("Abrindo o Google Maps...")
            falar("Abrindo o Google Maps.")
            webbrowser.open("https://www.google.com/maps")  # Abre o Google Maps

        else:
            # Reproduz o texto em fala
            falar(comando)
