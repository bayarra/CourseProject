# Add Mongolian language package compatible with the Spacy NLP toolkit as the alpha support model

## Goal
Add Mongolian language model compatible with Spacy NLP toolkit as alpha support. 
## Reason
spaCy is a free, open-source library for advanced Natural Language Processing framework in Python, which helps the developers to build real-world production-ready applications. The spaCy framework does not support the Mongolian language yet, not even alpha support. 
## What is alpha support?
In spaCy, languages marked as "alpha support" usually only include tokenization rules and various other rules and language data.

## Mongolian language
The Mongolian language has two alphabets, Mongolian Cyrillic and Traditional Mongolian scripts. In Mongolia, Mongolian Cyrillic is the official alphabet right now. This project includes the Mongolian Cyrillic transcript. 

## What’s included in this package?
Added Mongolian language into spaCy framework as  
    - code: mn
    - name: Mongolian

### Stop words
- stop_words.py  
List of most common words of a Mongolian language that are often useful to filter out, for example, "ба" or "нь." Matching tokens will return True for is_stop.
### Tokenizer exceptions
- tokenizer_exceptions.py  
Some Mongolian language's special-case rules for the tokenizer, for example, abbreviations with punctuation, like "г.м," abbreviations with upper cases, like "УИХ."
### Punctuation rules
- punctuation.py  
Regular expressions for splitting tokens. It includes rules for infixes.
### Lexical attributes
- lex_attrs.py  
Custom functions for setting lexical attributes on tokens, e.g., like_num, which includes numeric words in the Mongolian language, like "мянга" or "зуу."
### Examples
- examples.py  
Some sample words, sentences in the Mongolian language for testing inside the spaCy.
### Initialisation and linking class
- __init.py  
Create classes for Mongolian by linking the above language pieces of information. 

### Test cases
- test_tokenizer.py  
Test cases for tokenization for text in the Mongolian language.

### Usage sample
- test.py  

## Usage
    ```
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
        ```

## Has it been included in the spaCy officially yet?
No, not yet. Contributing to the spaCy community needs a lot of effort, and it is going in progress. 

## How to use it?
Because this package has not been officially included in spaCy yet, you need to clone the whole package and build it locally to use in your applications. 

### Where can I find the whole package?
You can clone the below link and build it locally, and then you can use it in your applications. 
    https://github.com/bayarra/spaCy.git

## Building the spaCy
- Required tools and packages:
    - C++ Build Tools  
        For Windows:
        - Download and install Visual Studio Build Tools
        - Install Desktop development with C++
    - python
    - cython. pip install Cython
    - and more...
- Build the spaCy  
    - Run the command `python setup.py build_ext --inplace`