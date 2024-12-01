#!/usr/bin/env python3
import re
class MyString:
    def __init__(self, value=''):
        self._value = None  
        self.value = value  

    @property
    def value(self):
        return self._value 

    @value.setter
    def value(self, value):
        if isinstance(value, str): 
            self._value = value
        else:
            print("The value must be a string.")
    def is_sentence(self):
        return self._value.endswith(".") if isinstance(self._value, str) else False
    def is_question(self):
        return self._value.endswith("?") if isinstance(self._value,str) else False
    def is_exclamation(self):
        return self._value.endswith("!") if isinstance(self._value,str) else False
           
    def count_sentences(self):
        sentences = re.findall(r'[.!?](?:\s|$)', self.value)
        return len(sentences)
