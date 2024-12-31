import speech_recognition as sr

# Inicializa o reconhecedor
recognizer = sr.Recognizer()

# Usa o microfone como fonte de áudio
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
    except sr.UnknownValueError:
        print("Desculpe, não consegui entender o que você disse.")
    except sr.RequestError:
        print("Não foi possível conectar ao serviço de reconhecimento de fala.")
