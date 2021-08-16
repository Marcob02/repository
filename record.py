from gtts import gTTS

def record(name, speech):
    gTTS(speech, lang="it").save(name+'.mp3')

if __name__ == '__main__':
    speech = input("Inserisci il dialogo che vuoi convertire in audio: \n")
    name = input('Inserisci il nome del file audio: ')
    record(name, speech)
