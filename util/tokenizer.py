"""
@author : Hyunwoong
@when : 2019-10-29
@homepage : https://github.com/gusdnd852
"""
import spacy
import en_core_web_sm
import de_core_news_sm

class Tokenizer:

    def __init__(self):
        self.spacy_de = de_core_news_sm.load()
        self.spacy_en = en_core_web_sm.load()

    def tokenize_de(self, text):
        """
        Tokenizes German text from a string into a list of strings
        """
        return [tok.text for tok in self.spacy_de.tokenizer(text)]

    def tokenize_en(self, text):
        """
        Tokenizes English text from a string into a list of strings
        """
        return [tok.text for tok in self.spacy_en.tokenizer(text)]
