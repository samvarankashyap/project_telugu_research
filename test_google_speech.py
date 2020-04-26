from google_speech import Speech

# say "Hello World"
#https://raw.githubusercontent.com/samvarankashyap/telugu/master/pustakalu/satakalu/sumathi_satakam.txt
import codecs
with codecs.open('sumathi_satakam.txt', encoding='utf-8') as f:
    for line in f:
        text = line
        lang = "te"
        speech = Speech(text, lang)
        #speech.play()
        sox_effects = ("speed", "1.05")
        speech.play(sox_effects)

"""
text = open("")
lang = "te"
speech = Speech(text, lang)
#speech.play()
sox_effects = ("speed", "1.05")
speech.play(sox_effects)
"""
