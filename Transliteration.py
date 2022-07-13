#pip install langdetect

from langdetect import detect

#pip install indic-nlp-library

from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator
from indicnlp.transliterate.unicode_transliterate import ItransTransliterator
#write any language to the input_text from google
#module is eligible for
#Assamese(as),Bangali(be),Gujarati(gu),Hidi/urdu(hi,ur)
#Marathi(ma),Nepali(ne),Odia(od),Punjab(pa),Sindhi(si),Sinhala(si),Sanskrit(sa)
#Konkani(ko),Kannada(ka),Malyalam(ma),Telugu(te),Tamil(ta)
input_text=('ఏమి చేస్తున్నారు')

# Transliterate from Native language to any other Indian languages
print(detect(input_text))
print(UnicodeIndicTransliterator.transliterate(input_text,"te","hi"))
#Transliterate from Native language to Roman script
print(ItransTransliterator.to_itrans(input_text,'te'))
