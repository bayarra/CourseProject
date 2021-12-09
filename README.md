# Add Mongolian language package compatible with the Spacy NLP toolkit as alpha support model

## Goal
Add Mongolian language model compatible with Spacy NLP toolkit as alpha support. 
## Reason
spaCy is a free, open-source library for advanced Natural Language Processing framework in Python, which helps the developers to build real-world production-ready applications. The spaCy framework does not support Mongolian language yet, not even as alpha support. 
## What is alpha support languages?
In spaCy, languages marked as "alpha support" usually only include tokenization rules and various other rules and language data.

## Mongolian language
Mongolian language has 2 alphabets, Mongolian Cyrillic, and Traditional Mongolian scripts. Mongolian Cyrillic is official alphabet in Mongolia right now. This project is includes the Mongolian Cyrillic transcript. 

## What is included in this package?
Added Mongolian language into spaCy framework as 
    - code: mn
    - name: Mongolian

### Stop words
- stop_words.py  
List of most common words of a Mongolian language that are often useful to filter out, for example “ба” or “нь”. Matching tokens will return True for is_stop.
### Tokenizer exceptions
- tokenizer_exceptions.py  
Some Mongolian language's special-case rules for the tokenizer, for example, abbreviations with punctuation, like “г.м”, abbreviations with upper cases, like "УИХ".
### Punctuation rules
- punctuation.py  
Regular expressions for splitting tokens. Includes rules for infixes.
### Lexical attributes
- lex_attrs.py  
Custom functions for setting lexical attributes on tokens, e.g. like_num, which includes numeric words in Mongolian language, like “мянга” or “зуу”.
### Examples
- examples.py  
Some sample words, sentences in Mongolian language for testing inside the spaCy.
### Initialation and linking class
- __init.py  
Create classes for Mongolian with linking above language informations. 

### Test cases
- test_tokenizer.py  
Test cases for tokenization for text in Mongolian language.

### Usage sample
- test.py  

## Usage
    ```
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
    ```

## Does it included the spaCy official yet?
No, not yet. Working on it. Contributing the spaCy community needs a lot efforts, and it is going in progress. 

## How to use it?
Because of this package has not officially included in spaCy yet, you will needed to clone the whole package and build locally. 

### Where can I find the whole package?
You can clone below link and build it locally, and then you can use in your applications. 
    https://github.com/bayarra/spaCy.git
