import spacy
from spacy.lang.en import Mongolian

nlp = Mongolian()

print(nlp.lang) 
# output will be:
    # mn
print(nlp) 
# output will be:
    # <spacy.lang.mn.Mongolian object at 0x0000018A469C5130>

my_txt = "Монгол хэл нь Монгол улсын албан ёсны хэл юм."
my_doc = nlp(my_txt)

for token in my_doc:
    print(token.text)

    # Монгол 
    # хэл
    # нь
    # Монгол
    # улсын
    # албан
    # ёсны
    # хэл
    # юм
    # .
