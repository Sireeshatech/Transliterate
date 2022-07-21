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
    print(transliterate(text,sanscript.DEVANAGARI,sanscript.VELTHUIS))
elif langdetect=='pa':
    print("\nGiven Language is : PUNJABI")
    print(transliterate(text,sanscript.PUNJABI,sanscript.VELTHUIS))
elif langdetect=='gu':
    print("\nGiven Language is : GUJARATI")
    print(transliterate(text,sanscript.GUJARATI,sanscript.VELTHUIS))
elif langdetect=='kn':
    print("\nGiven Language is : KANNADA")
    print(transliterate(text,sanscript.KANNADA,sanscript.VELTHUIS))
elif langdetect=='ml':
    print("\nGiven Language is : MALAYALAM")
    print(transliterate(text,sanscript.MALAYALAM,sanscript.VELTHUIS))
elif langdetect=='bn':
    print("\nGiven Language is : BENGALI")
    print(transliterate(text,sanscript.BENGALI,sanscript.VELTHUIS))
elif langdetect=='te':
    print("\nGiven Language is : TELUGU")
    print(transliterate(text,sanscript.TELUGU,sanscript.VELTHUIS))
elif langdetect=='ta':
    print("\nGiven Language is : TAMIL")
    print(transliterate(text,sanscript.TAMIL,sanscript.VELTHUIS))
elif langdetect=='or':
    print("\nGiven Language is : ORIYA")
    print(transliterate(text,sanscript.ORIYA,sanscript.VELTHUIS))
else:
    print("Can't able to transliterate this language")
