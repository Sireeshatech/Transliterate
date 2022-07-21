#Language Transliteration
#pip install indic-transliteration
#pip install langdetect
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
from langdetect import detect

text = input("Enter text in any INDIAN languages : ")

langdetect=detect(text)

#Languages={'DEVANAGARI':'hi','PUNJABI':'pa','GUJARATI':'gu', 'KANNADA':'kn',
#'MALAYALAM':'ml','BENGALI':'bn','TELUGU':'te','TAMIL':'ta','ORIYA':'or'}

# printing the transliterated text with the name of the input language
if langdetect=='hi':
    print("\nGiven Language is : HINDI\n")
    print(transliterate(text,sanscript.DEVANAGARI,sanscript.ITRANS))
elif langdetect=='pa':
    print("\nGiven Language is : PUNJABI")
    print(transliterate(text,sanscript.PUNJABI,sanscript.ITRANS))
elif langdetect=='gu':
    print("\nGiven Language is : GUJARATI")
    print(transliterate(text,sanscript.GUJARATI,sanscript.ITRANS))
elif langdetect=='kn':
    print("\nGiven Language is : KANNADA")
    print(transliterate(text,sanscript.KANNADA,sanscript.ITRANS))
elif langdetect=='ml':
    print("\nGiven Language is : MALAYALAM")
    print(transliterate(text,sanscript.MALAYALAM,sanscript.ITRANS))
elif langdetect=='bn':
    print("\nGiven Language is : BENGALI")
    print(transliterate(text,sanscript.BENGALI,sanscript.ITRANS))
elif langdetect=='te':
    print("\nGiven Language is : TELUGU")
    print(transliterate(text,sanscript.TELUGU,sanscript.ITRANS))
elif langdetect=='ta':
    print("\nGiven Language is : TAMIL")
    print(transliterate(text,sanscript.TAMIL,sanscript.ITRANS))
elif langdetect=='or':
    print("\nGiven Language is : ORIYA")
    print(transliterate(text,sanscript.ORIYA,sanscript.ITRANS))
else:
    print("Can't able to transliterate this language")
