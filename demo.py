import spacy
from spacy.lang.mn import Mongolian

nlp = Mongolian()

print(nlp.lang) 
# output will be:
    # mn
print(nlp) 
# output will be:
    # <spacy.lang.mn.Mongolian object at 0x0000018A469C5130>

my_txt = "Монгол хэлэнд үндсэн хоёр бичиг бий. Кирил үсгийг 1940 оноос үзэж эхлэв."
my_doc = nlp(my_txt)

print('Token\t\tStop\tPunct\tDigit\tLikeNum\tTitle')
for token in my_doc:
    print(token.text,'\t\t',token.is_stop,'\t',token.is_punct,'\t',token.is_digit,'\t',token.like_num,'\t', token.is_title)

    # Token           Stop    Punct   Digit   LikeNum Title
    # Монгол           False   False   False   False   True
    # хэлэнд           False   False   False   False   False
    # үндсэн           False   False   False   False   False
    # хоёр             False   False   False   True    False
    # бичиг            False   False   False   False   False
    # бий              False   False   False   False   False
    # .                False   True    False   False   False
    # Кирил            False   False   False   False   True
    # үсгийг           False   False   False   False   False
    # 1940             False   False   True    True    False
    # оноос            False   False   False   False   False
    # үзэж             False   False   False   False   False
    # эхлэв            False   False   False   False   False
    # .                False   True    False   False   False