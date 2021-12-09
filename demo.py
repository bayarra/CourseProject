import spacy
from spacy.lang.mn import Mongolian
# importing the Mongolian language model

nlp = Mongolian()
# defining Mongolian NLP

print(nlp.lang) 
# Output:
    # mn
print(nlp) 
# Output:
    # <spacy.lang.mn.Mongolian object at 0x0000018A469C5130>

# Some Mongolian cyrillic text:
my_txt = ("Монгол хэл нь үндсэн хоёр бичиг бүхий байна."+
            "Кирил үсгийг 1940 оноос л үзэж эхлэв.")

my_doc = nlp(my_txt)

# Printing some token attributes:
print('Token\t\tStop\tPunct\tDigit\tLikeNum\tTitle')
for token in my_doc:
    print(token.text,'\t\t',token.is_stop,'\t',token.is_punct,'\t',token.is_digit,'\t',token.like_num,'\t', token.is_title)
# Output:
    # Token           Stop    Punct   Digit   LikeNum Title
    # Монгол           False   False   False   False   True
    # хэл              False   False   False   False   False
    # нь               True    False   False   False   False
    # үндсэн           False   False   False   False   False
    # хоёр             False   False   False   True    False
    # бичиг            False   False   False   False   False
    # бүхий            False   False   False   False   False
    # байна            True    False   False   False   False
    # .                False   True    False   False   False
    # Кирил            False   False   False   False   True
    # үсгийг           False   False   False   False   False
    # 1940             False   False   True    True    False
    # оноос            False   False   False   False   False
    # л                True    False   False   False   False
    # үзэж             False   False   False   False   False
    # эхлэв            False   False   False   False   False
    # .                False   True    False   False   False

# Remove stop words & punctuations:
cleaned = [token for token in my_doc if not token.is_stop and not token.is_punct]

for token in cleaned:
    print(token.text)
# Output:
    # Монгол
    # хэл
    # үндсэн
    # хоёр
    # бичиг
    # бүхий
    # Кирил
    # үсгийг
    # 1940
    # оноос
    # үзэж
    # эхлэв