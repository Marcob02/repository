import speech_recognition as sr

def main():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        #r.adjust_for_ambient_noise(source)
        r.energy_threshold = 10000
        #print("Energy threshold set to: ", r.energy_threshold)
        while True:
            print("Speak Anything :")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language="it-IT")
                text = text.lower()
                if text == "esci": break
                print("You said : {}".format(text))
            except:
                print("Sorry could not recognize what you said")

if __name__ == '__main__':
    main()
