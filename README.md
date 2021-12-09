# Add Mongolian language package compatible with the Spacy NLP toolkit as alpha support model

## Goal
Add Mongolian language model compatible with Spacy NLP toolkit as alpha support. 
## Reason
The spaCy framework does not support Mongolian language yet. 
## What is alpha support languages?
Languages marked as "alpha support" usually only include tokenization rules and various other rules and language data.

## What is included
  - Added Mongolian language into spaCy framework as 
    - code: mn
    - name: Mongolian

## Stop words
    stop_words.py	
    List of most common words of a Mongolian language that are often useful to filter out, for example “ба” or “нь”. Matching tokens will return True for is_stop.
## Tokenizer exceptions
    tokenizer_exceptions.py	
    Some Mongolian language's special-case rules for the tokenizer, for example, abbreviations with punctuation, like “г.м”, abbreviations with upper cases, like "УИХ".
## Punctuation rules
    punctuation.py	
    Regular expressions for splitting tokens. Includes rules for infixes.
## Lexical attributes
    lex_attrs.py	
    Custom functions for setting lexical attributes on tokens, e.g. like_num, which includes numeric words in Mongolian language, like “мянга” or “зуу”.
## Examples
    examples.py 
    Some sample words, sentences in Mongolian language for testing inside the spaCy.
## Initialation and linking class
    __init.py

## Test cases
    test_tokenizer.py
    Test cases for tokenization for text in Mongolian language.

## Usage sample
    test.py

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
    No, not yet. Working on it. 

## How to use it?
    Because of this package has not officially included in spaCy yet, you will needed to clone whole package and build locally. 