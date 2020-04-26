from googletrans import Translator
translator = Translator()
kk = translator.translate('안녕하세요.')
print(kk.text)
kk = translator.translate('చూశారా')
print(kk.text)
